import os
from abc import ABC, abstractmethod
from audioman.metadata.metadata import Metadata
from mutagen import File
from mutagen.id3 import ID3, POPM, TIT2, TPE1, TALB, TDRC


class Tagger(ABC):

    @abstractmethod
    def __init__(self, file):
        pass

    @abstractmethod
    def tag(self, metadata: Metadata):
        pass

    @abstractmethod
    def save(self):
        pass


class AudioTagger:

    @staticmethod
    def get_tagger(file) -> Tagger:
        # Get the extension of file
        ext = os.path.basename(file).rpartition(".")[-1].lower()
        if ext in ["ogg", "asf", "flac", "mp4", "m4a", "m4b", "m4p", "tak"]:
            return NonID3Tagger(file)
        elif ext in ["aac", "ac3", "aiff", "dff", "dsf", "tta"]:
            return ID3CompatibleFileTagger(file)
        else:
            return ID3Tagger(file)


class ID3Tagger(Tagger):
    """
    The Tagger that adds Metadata
    to ID3 compatible Audio files
    """

    def __init__(self, file):
        self.file = ID3(file)
        self.audio = self.file

    def tag(self, metadata: Metadata):
        self.audio.add(TIT2(encoding=3, text=metadata.title))
        self.audio.add(TPE1(encoding=3, text=metadata.artist))
        self.audio.add(TALB(encoding=3, text=metadata.album))
        self.audio.add(TDRC(encoding=3, text=metadata.date))
        self.audio.add(POPM(rating=metadata.rating))

    def save(self):
        self.file.save()


class NonID3Tagger(Tagger):
    """The Tagger that adds Metadata
    to non ID3 compatible Audio files ('ogg', 'aasf')"""

    def __init__(self, file):
        self.audio = File(file)

    def tag(self, metadata: Metadata):
        self.audio["title"] = metadata.title
        self.audio["artist"] = metadata.artist
        self.audio["album"] = metadata.album
        self.audio["rating"] = str(metadata.rating)
        self.audio["date"] = metadata.date

    def save(self):
        self.audio.save()


class ID3CompatibleFileTagger(Tagger):

    def __init__(self, file):
        self.file = File(file)
        if self.file.tags is None:
            self.file.add_tags()
        self.audio = self.file.tags

    def tag(self, metadata: Metadata):
        self.audio.add(TIT2(encoding=3, text=metadata.title))
        self.audio.add(TPE1(encoding=3, text=metadata.artist))
        self.audio.add(TALB(encoding=3, text=metadata.album))
        self.audio.add(TDRC(encoding=3, text=metadata.date))
        self.audio.add(POPM(rating=metadata.rating))

    def save(self):
        self.file.save()
