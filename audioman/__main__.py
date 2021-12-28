import asyncio
import sys
from typing import List, Optional

import typer
from rich.console import Console

from audioman.cli import CLITools
from audioman.fingerprint.identifier import AudioFileIdentifier
from audioman.locator.audio_file_locator import AudioFileLocator
from audioman.lookup.metadata_lookup import MetadataLookup

console = Console()


def main(source: str,
         exclude: Optional[List[str]] = typer.Option([],
                                                     "--exclude", "-e",
                                                     help="Files or Directories to exclude",
                                                     case_sensitive=False)):
    # Print the logo
    typer.echo(CLITools.logo)
    print(exclude)

    # File detection
    files = AudioFileLocator(source, exclude).locate_files()
    if len(files) == 0:
        console.print("[red bold]Quit: No audio files found!")
        sys.exit(1)

    # User config
    # folderstruct = CLITools.folder_structure_chooser()
    # filestruct = CLITools.file_structure_chooser()

    # Restructuring
    ids = []
    for file in files:
        identifier = AudioFileIdentifier(file)
        mb_id = identifier.identify()
        ids.append(mb_id)

    print(asyncio.run(get_all_metadata(ids)))


async def get_all_metadata(ids: list):
    result = await asyncio.gather(*(MetadataLookup.lookup(file_id) for file_id in ids))
    return result


if __name__ == "__main__":
    typer.run(main)
