from InquirerPy import inquirer

from audioman.files.structure import FolderStructure, FileNameStructure
from audioman.parser.metadata_parser import AlbumChooser


class TerminalAlbumChooser(AlbumChooser):  # pylint: disable=too-few-public-methods

    def __init__(self, file):
        self.__choices = []
        self.file = file
        self.__album_lists = []

    def choose_album(self, albums: list) -> list:
        self.__album_lists = albums
        if len(albums) == 1:
            return albums[0]
        for i in range(len(albums)):  # pylint: disable=consider-using-enumerate
            if 'date' in albums[i]:
                self.__choices.append(
                    {"name": f"{albums[i]['title']} - {albums[i]['date']}", "value": i})
            else:
                self.__choices.append(
                    {"name": f"{albums[i]['title']}", "value": i})

        return self.__select_album_cli()

    def __select_album_cli(self) -> list:
        print(f"The file {self.file} has multiple Albums available")
        result = inquirer.select(
            message="Select the album",
            choices=self.__choices
        ).execute()
        return self.__album_lists[result]


class CLITools:
    logo = """
 █████╗ ██╗   ██╗██████╗ ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██╔══██╗██║   ██║██╔══██╗██║██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
███████║██║   ██║██║  ██║██║██║   ██║██╔████╔██║███████║██╔██╗ ██║
██╔══██║██║   ██║██║  ██║██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║╚██████╔╝██████╔╝██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝                                                                
"""

    @staticmethod
    def folder_structure_chooser():
        folders = [{"name": struct.human_readable(), "value": struct}
                   for struct in FolderStructure]
        return inquirer.select(message="Select a folder structure",
                               choices=folders, default=FolderStructure.ARTIST__ALBUM).execute()

    @staticmethod
    def file_structure_chooser():
        files = [{"name": struct.human_readable(), "value": struct}
                 for struct in FileNameStructure]
        return inquirer.select(message="Select a filename structure",
                               choices=files, default=FileNameStructure.NR_TITLE).execute()
