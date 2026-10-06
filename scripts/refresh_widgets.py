"""Refresh profile cards without replacing valid snapshots with error responses."""

import shutil
import sys
from http.client import HTTPException
from pathlib import Path
from urllib.request import Request, urlopen
from xml.etree import ElementTree

WIDGETS = {
    "spotify.svg": (
        "https://spotify-recently-played.jeffreyca.workers.dev/svg"
        "?user=an3l6poe03o6g6htrdrs0hgjy&count=4&unique=1&width=300"
        "&time=0&now_playing=0&profile=off",
        "Last played on Spotify:",
    ),
    "streak.svg": (
        "https://streak-stats.demolab.com?user=Majkey25&theme=dracula",
        "Current Streak",
    ),
}


def validate_svg(content: bytes, expected_text: str) -> None:
    root = ElementTree.fromstring(content)
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError("Response is not an SVG")
    text = root.get("aria-label", "") + " ".join(root.itertext())
    if expected_text not in text:
        raise ValueError("Response is missing the expected card content")


def refresh_widgets(previous: Path, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    for filename, (url, expected_text) in WIDGETS.items():
        destination = output / filename
        backup = previous / filename
        if backup.is_file():
            validate_svg(backup.read_bytes(), expected_text)
            shutil.copyfile(backup, destination)
        try:
            request = Request(url, headers={"User-Agent": "Majkey25-profile-widgets"})
            with urlopen(request, timeout=30) as response:
                content = response.read(2_000_001)
            if len(content) > 2_000_000:
                raise ValueError("Response exceeds 2 MB")
            validate_svg(content, expected_text)
        except (OSError, HTTPException, ValueError, ElementTree.ParseError) as error:
            if not destination.is_file():
                raise RuntimeError(f"No valid snapshot for {filename}") from error
            print(
                f"::warning::{filename}: {type(error).__name__}; keeping previous snapshot"
            )
            continue
        destination.write_bytes(content)
        print(f"Updated {filename}")


if __name__ == "__main__":
    refresh_widgets(Path(sys.argv[1]), Path(sys.argv[2]))
