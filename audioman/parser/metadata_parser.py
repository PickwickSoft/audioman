from audioman.metadata.metadata import Metadata

class MetadataParser:

    def __init__(self, data):
        self.data = data

    def parse_metadata(self) -> Metadata:
        metadata = Metadata()
        metadata.title = self.__parse_for_title()
        metadata.artist = self.__parse_for_artist()
        metadata.recording_id = self.__parse_for_recording_id()
        metadata.rating = self.__parse_for_rating()
        return metadata

    def __parse_for_title(self) -> str:
        return self.data['recording']['title']

    def __parse_for_artist(self) -> str:
        return self.data['recording']['artist-credit'][0]['artist']['name']

    def __parse_for_recording_id(self) -> str:
        return self.data['recording']['id']

    def __parse_for_rating(self) -> str:
        if 'rating' in self.data['recording']:
            return self.data['recording']['rating']['rating']
