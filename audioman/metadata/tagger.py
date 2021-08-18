from mutagen.id3 import ID3, TIT2, POPM, TPE1
from audioman.metadata.metadata import Metadata


class AudioFileTagger:
    """
    The Tagger that adds Metadata to Audio files
    """

    def __init__(self, file):
        self.audio = ID3(file)

    def tag(self, metadata: Metadata):
        self.audio.add(TIT2(encoding=3, text=metadata.title))
        self.audio.add(TPE1(encoding=3, text=metadata.artist))
        self.audio.add(POPM(rating=metadata.rating))

    def save(self):
        self.audio.save()