import typer
from typing import List, Optional
from audioman.cli import CLITools
from audioman.locator.audio_file_locator import AudioFileLocator


def main(source: str,
         exclude: Optional[List[str]] = typer.Option([], "--exclude", "-e", help="Files or Directories to exclude",
                                                     case_sensitive=False)):
    # Print the logo
    typer.echo(CLITools.logo)
    print(exclude)
    files = AudioFileLocator(source, exclude).locate_files()
    folderstruct = CLITools.folder_structure_chooser()
    filestruct = CLITools.file_structure_chooser()


if __name__ == "__main__":
    typer.run(main)
