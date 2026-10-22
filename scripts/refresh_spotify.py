"""Refresh the Spotify card while retaining a valid snapshot during outages."""

import subprocess
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree

SPOTIFY_URL = (
    "https://spotify-recently-played.jeffreyca.workers.dev/svg"
    "?user=an3l6poe03o6g6htrdrs0hgjy&count=4&unique=1&width=300"
    "&time=0&now_playing=0&profile=off"
)
FETCH_TIMEOUT_SECONDS = 30


def fetch_card() -> bytes:
    # A socket timeout alone allows an endless trickle of response bytes.
    return subprocess.run(
        [sys.executable, __file__, "--fetch", SPOTIFY_URL],
        capture_output=True,
        check=True,
        timeout=FETCH_TIMEOUT_SECONDS,
    ).stdout


def validate_card(content: bytes) -> None:
    root = ElementTree.fromstring(content)
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError("Response is not an SVG")
    if not root.get("aria-label", "").startswith("Last played on Spotify:"):
        raise ValueError("Response does not contain a Spotify history card")


def refresh_spotify(previous: Path, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    destination = output / "spotify.svg"
    backup = previous / "spotify.svg"
    try:
        content = fetch_card()
        if len(content) > 2_000_000:
            raise ValueError("Response exceeds 2 MB")
        validate_card(content)
    except (
        OSError,
        subprocess.SubprocessError,
        ValueError,
        ElementTree.ParseError,
    ) as error:
        try:
            snapshot = backup if backup.is_file() else destination
            content = snapshot.read_bytes()
            validate_card(content)
        except (OSError, ValueError, ElementTree.ParseError) as backup_error:
            raise RuntimeError("No valid Spotify snapshot") from backup_error
        if snapshot != destination:
            destination.write_bytes(content)
        print(f"::warning::Spotify: {type(error).__name__}; keeping previous snapshot")
        return
    destination.write_bytes(content)
    print("Updated spotify.svg")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--fetch":
        request = Request(
            sys.argv[2], headers={"User-Agent": "Majkey25-profile-widgets"}
        )
        with urlopen(request, timeout=FETCH_TIMEOUT_SECONDS) as response:
            sys.stdout.buffer.write(response.read(2_000_001))
    else:
        refresh_spotify(Path(sys.argv[1]), Path(sys.argv[2]))
