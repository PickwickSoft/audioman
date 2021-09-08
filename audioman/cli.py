from InquirerPy import inquirer
from audioman.parser.metadata_parser import AlbumChooser


class TerminalAlbumChooser(AlbumChooser):   # pylint: disable=too-few-public-methods

    def __init__(self, file):
        self.__choices = []
        self.file = file
        self.__album_lists = []

    def choose_album(self, albums: list) -> list:
        self.__album_lists = albums
        if len(albums) == 1:
            return albums[0]
        for i in range(len(albums)):   # pylint: disable=consider-using-enumerate
            if 'date' in albums[i]:
                self.__choices.append(
                    {"name": "{0} - {1}".format(albums[i]['title'], albums[i]['date']), "value": i})
            else:
                self.__choices.append(
                    {"name": "{0}".format(albums[i]['title']), "value": i})

        return self.__select_album_cli()

    def __select_album_cli(self) -> list:
        print("The file {} has multiple Albums available".format(self.file))
        result = inquirer.select(
            message="Select the album",
            choices=self.__choices
        ).execute()
        return self.__album_lists[result]
