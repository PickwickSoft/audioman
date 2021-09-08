from InquirerPy import inquirer
from audioman.parser.metadata_parser import AlbumChooser

class TerminalAlbumChooser(AlbumChooser):

    def __init__(self, file):
        self.choices = []
        self.file = file
        self.album_lists = []

    def choose_album(self, albums: list) -> list:
        self.album_lists = albums
        for i in range(len(albums)):
            if 'date' in albums[i]:
                self.choices.append({"name": "{0} - {1}".format(albums[i]['title'], albums[i]['date']), "value": i})
            else:
                self.choices.append(
                    {"name": "{0}".format(albums[i]['title']), "value": i})

        return self.__select_album_cli()

    def __select_album_cli(self) -> list:
        print("The file {} has multiple Albums available".format(self.file))
        result = inquirer.select(
            message="Select the album",
            choices=self.choices
        ).execute()
        return self.album_lists[result]
