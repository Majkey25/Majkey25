"""Regression check: a failed provider must never erase the previous card."""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
from urllib.error import URLError

from refresh_widgets import WIDGETS, refresh_widgets


class WidgetRefreshTest(unittest.TestCase):
    def test_refresh_and_last_good_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            previous = Path(directory) / "previous"
            previous.mkdir()
            output = Path(directory) / "output"
            old = b'<svg xmlns="http://www.w3.org/2000/svg"><text>old card</text>'
            snapshots = {
                filename: old + f"<text>{marker}</text></svg>".encode()
                for filename, (_, marker) in WIDGETS.items()
            }
            for filename, content in snapshots.items():
                (previous / filename).write_bytes(content)
            fresh = [
                content.replace(b"old card", b"new card")
                for content in snapshots.values()
            ]
            with patch(
                "refresh_widgets.urlopen",
                side_effect=[io.BytesIO(card) for card in fresh],
            ):
                refresh_widgets(previous, output)
            self.assertEqual(
                [(output / filename).read_bytes() for filename in WIDGETS], fresh
            )
            failures = (
                URLError("offline"),
                b"<html>Unavailable</html>",
                b"<svg",
                b'<svg xmlns="http://www.w3.org/2000/svg"><text>Error</text></svg>',
                b"x" * 2_000_001,
            )
            for failure in failures:
                with self.subTest(failure=type(failure).__name__):
                    responses = (
                        [io.BytesIO(failure), io.BytesIO(failure)]
                        if isinstance(failure, bytes)
                        else [failure, failure]
                    )
                    with (
                        patch("refresh_widgets.urlopen", side_effect=responses),
                        redirect_stdout(io.StringIO()),
                    ):
                        refresh_widgets(previous, output)
                    for filename, content in snapshots.items():
                        self.assertEqual((output / filename).read_bytes(), content)
            with (
                patch(
                    "refresh_widgets.urlopen",
                    side_effect=[URLError("offline"), io.BytesIO(fresh[1])],
                ),
                redirect_stdout(io.StringIO()),
            ):
                refresh_widgets(previous, output)
            self.assertEqual(
                (output / "spotify.svg").read_bytes(), snapshots["spotify.svg"]
            )
            self.assertEqual((output / "streak.svg").read_bytes(), fresh[1])
            with patch("refresh_widgets.urlopen", side_effect=URLError("offline")):
                with self.assertRaisesRegex(RuntimeError, "No valid snapshot"):
                    refresh_widgets(
                        Path(directory) / "missing", Path(directory) / "empty"
                    )


if __name__ == "__main__":
    unittest.main()
