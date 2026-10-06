"""Refresh the Spotify card while retaining a valid snapshot during outages."""

import shutil
import sys
from http.client import HTTPException
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree

SPOTIFY_URL = (
    "https://spotify-recently-played.jeffreyca.workers.dev/svg"
    "?user=an3l6poe03o6g6htrdrs0hgjy&count=4&unique=1&width=300"
    "&time=0&now_playing=0&profile=off"
)


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
    if backup.is_file():
        validate_card(backup.read_bytes())
        shutil.copyfile(backup, destination)
    try:
        request = Request(
            SPOTIFY_URL, headers={"User-Agent": "Majkey25-profile-widgets"}
        )
        with urlopen(request, timeout=30) as response:
            content = response.read(2_000_001)
        if len(content) > 2_000_000:
            raise ValueError("Response exceeds 2 MB")
        validate_card(content)
    except (OSError, HTTPException, ValueError, ElementTree.ParseError) as error:
        if not destination.is_file():
            raise RuntimeError("No valid Spotify snapshot") from error
        print(f"::warning::Spotify: {type(error).__name__}; keeping previous snapshot")
        return
    destination.write_bytes(content)
    print("Updated spotify.svg")


if __name__ == "__main__":
    refresh_spotify(Path(sys.argv[1]), Path(sys.argv[2]))
