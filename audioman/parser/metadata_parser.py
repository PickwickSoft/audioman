from abc import ABC, abstractmethod
from audioman.metadata.metadata import Metadata


class AlbumChooser(ABC):

    @abstractmethod
    def choose_album(self, albums: list) -> list:
        pass


class MetadataParser:

    def __init__(self, data, album_chooser: AlbumChooser):
        self.data = data
        self.chooser = album_chooser
        self.release = []

    def parse_metadata(self) -> Metadata:
        metadata = Metadata()
        metadata.title = self.__parse_for_title()
        metadata.artist = self.__parse_for_artist()
        metadata.recording_id = self.__parse_for_recording_id()
        metadata.rating = self.__parse_for_rating()
        metadata.album = self.__parse_for_album()
        metadata.date = self.__parse_for_date()
        return metadata

    def __parse_for_title(self) -> str:
        return self.data['recording']['title']

    def __parse_for_artist(self) -> str:
        return self.data['recording']['artist-credit'][0]['artist']['name']

    def __parse_for_recording_id(self) -> str:
        return self.data['recording']['id']

    def __parse_for_rating(self) -> int:
        if 'rating' in self.data['recording']:
            return int(self.data['recording']['rating']['rating'])
        return 0

    def __parse_for_album(self) -> str:
        if self.data['recording']['release-count'] != 0:
            self.release = self.chooser.choose_album(self.data['recording']['release-list'])
            return self.release["title"]
    
    def __parse_for_date(self) -> str:
        if self.release != [] and "date" in self.release:
            return self.release["date"]
        return ""
