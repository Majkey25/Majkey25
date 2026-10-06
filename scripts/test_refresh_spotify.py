"""Check that provider outages and error cards preserve the last valid image."""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
from urllib.error import URLError

from refresh_spotify import refresh_spotify


class SpotifyRefreshTest(unittest.TestCase):
    def test_refresh_and_outage_fallback(self) -> None:
        card = (
            b'<svg xmlns="http://www.w3.org/2000/svg" '
            b'aria-label="Last played on Spotify: example"><text>old</text></svg>'
        )
        fresh = card.replace(b"old", b"new")
        with tempfile.TemporaryDirectory() as directory:
            previous = Path(directory) / "previous"
            previous.mkdir()
            (previous / "spotify.svg").write_bytes(card)
            output = Path(directory) / "output"
            with patch("refresh_spotify.urlopen", return_value=io.BytesIO(fresh)):
                refresh_spotify(previous, output)
            self.assertEqual((output / "spotify.svg").read_bytes(), fresh)
            for failure in (
                URLError("offline"),
                b"<html>Unavailable</html>",
                b"<svg",
                b'<svg xmlns="http://www.w3.org/2000/svg"><text>Error</text></svg>',
                b"x" * 2_000_001,
            ):
                with (
                    self.subTest(failure=type(failure).__name__),
                    patch(
                        "refresh_spotify.urlopen",
                        side_effect=[
                            io.BytesIO(failure)
                            if isinstance(failure, bytes)
                            else failure
                        ],
                    ),
                    redirect_stdout(io.StringIO()),
                ):
                    refresh_spotify(previous, output)
                self.assertEqual((output / "spotify.svg").read_bytes(), card)
            with patch("refresh_spotify.urlopen", side_effect=URLError("offline")):
                with self.assertRaisesRegex(RuntimeError, "No valid Spotify snapshot"):
                    refresh_spotify(
                        Path(directory) / "missing", Path(directory) / "empty"
                    )


if __name__ == "__main__":
    unittest.main()
