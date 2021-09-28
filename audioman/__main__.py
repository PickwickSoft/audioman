import typer
from InquirerPy import inquirer
from audioman.cli import CLITools
from audioman.files.structure import FileNameStructure, FolderStructure


def main(source: str):
    # Print the logo
    typer.echo(CLITools.logo)
    folders = [{"name": struct.human_readable(), "value": struct}
               for struct in FolderStructure]
    files = [{"name": struct.human_readable(), "value": struct}
             for struct in FileNameStructure]
    folder_structure = inquirer.select(message="Select a folder structure",
                    choices=folders, default=FolderStructure.ARTIST__ALBUM).execute()
    file_structure = inquirer.select(message="Select a filename structure",
                                       choices=files, default=FileNameStructure.NR_TITLE).execute()


if __name__ == "__main__":
    typer.run(main)
