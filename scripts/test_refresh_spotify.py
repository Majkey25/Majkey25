"""Check that provider outages and error cards preserve the last valid image."""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Event, Thread
from time import monotonic
from unittest.mock import patch
from urllib.error import URLError

from refresh_spotify import refresh_spotify


class SpotifyRefreshTest(unittest.TestCase):
    def test_corrupt_snapshot_does_not_block_refresh(self) -> None:
        fresh = (
            b'<svg xmlns="http://www.w3.org/2000/svg" '
            b'aria-label="Last played on Spotify: example"><text>new</text></svg>'
        )
        with tempfile.TemporaryDirectory() as directory:
            previous = Path(directory) / "previous"
            previous.mkdir()
            (previous / "spotify.svg").write_bytes(b"<svg")
            output = Path(directory) / "output"
            with patch("refresh_spotify.fetch_card", return_value=fresh):
                refresh_spotify(previous, output)
            self.assertEqual((output / "spotify.svg").read_bytes(), fresh)
            with patch("refresh_spotify.fetch_card", side_effect=URLError("offline")):
                with self.assertRaisesRegex(RuntimeError, "No valid Spotify snapshot"):
                    refresh_spotify(previous, Path(directory) / "empty")
                with patch.object(
                    Path, "write_bytes", side_effect=PermissionError("read-only")
                ):
                    refresh_spotify(Path(directory) / "missing", output)
            self.assertEqual((output / "spotify.svg").read_bytes(), fresh)

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
            with patch("refresh_spotify.fetch_card", return_value=fresh):
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
                        "refresh_spotify.fetch_card",
                        side_effect=[failure],
                    ),
                    redirect_stdout(io.StringIO()),
                ):
                    refresh_spotify(previous, output)
                self.assertEqual((output / "spotify.svg").read_bytes(), card)
            with patch("refresh_spotify.fetch_card", side_effect=URLError("offline")):
                with self.assertRaisesRegex(RuntimeError, "No valid Spotify snapshot"):
                    refresh_spotify(
                        Path(directory) / "missing", Path(directory) / "empty"
                    )

    def test_real_http_refresh_and_slow_response_fallback(self) -> None:
        fresh = (
            b'<svg xmlns="http://www.w3.org/2000/svg" '
            b'aria-label="Last played on Spotify: example"><text>new</text></svg>'
        )
        stopped = Event()
        requested = Event()
        disconnected = Event()

        class Provider(BaseHTTPRequestHandler):
            def do_GET(self) -> None:
                requested.set()
                if self.path != "/slow-headers":
                    self.send_response(200)
                    self.end_headers()
                if self.path == "/fresh":
                    self.wfile.write(fresh)
                    return
                try:
                    while not stopped.wait(0.05):
                        self.wfile.write(b"x")
                        self.wfile.flush()
                except OSError:
                    disconnected.set()

        with ThreadingHTTPServer(("127.0.0.1", 0), Provider) as server:
            thread = Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                with tempfile.TemporaryDirectory() as directory:
                    previous = Path(directory) / "previous"
                    previous.mkdir()
                    old = fresh.replace(b"new", b"old")
                    (previous / "spotify.svg").write_bytes(old)
                    output = Path(directory) / "output"
                    for route in ("fresh", "slow-body", "slow-headers"):
                        requested.clear()
                        disconnected.clear()
                        with (
                            self.subTest(route=route),
                            patch("refresh_spotify.FETCH_TIMEOUT_SECONDS", 1),
                            patch(
                                "refresh_spotify.SPOTIFY_URL",
                                f"http://127.0.0.1:{server.server_port}/{route}",
                            ),
                            redirect_stdout(io.StringIO()) as messages,
                        ):
                            started = monotonic()
                            refresh_spotify(previous, output)
                            self.assertLess(monotonic() - started, 4)
                            self.assertTrue(requested.is_set())
                            self.assertEqual(
                                (output / "spotify.svg").read_bytes(),
                                fresh if route == "fresh" else old,
                            )
                            if route != "fresh":
                                self.assertIn("TimeoutExpired", messages.getvalue())
                                self.assertTrue(disconnected.wait(2))
            finally:
                stopped.set()
                server.shutdown()
                thread.join()


if __name__ == "__main__":
    unittest.main()
