from enum import Enum


class StructureElement:
    pass


class FolderStructure(StructureElement, Enum):
    """Enum containing possible folder hierarchies:
    ``__`` is a placeholder for ``/`` and ``_`` is the placeholder for `` - ``"""

    def human_readable(self):
        return self.name.replace("__", "/").replace(
            "_", " - ")

    ARTIST__ARTIST_ALBUM = 0
    ARTIST__ALBUM = 1
    ARTIST_ALBUM = 2
    ALBUM = 3
    ARTIST = 4


class FileNameStructure(StructureElement, Enum):
    """Enum containing possible file name templates
    ``_`` is a placeholder for `` - `` and ``__`` is the placeholder for ``.``.

    ``ARTIST_ALBUM_NR_TITLE`` is a special case for ``Artist (Album) - Number - Title``"""

    def human_readable(self):
        if self == self.ARTIST_ALBUM_NR_TITLE:
            return "ARTIST (ALBUM) - NR - TITLE"
        return self.name.replace("__", ".").replace("_", " - ")

    NR_TITLE = 0
    ARTIST_TITLE = 1
    ARTIST_NR_TITLE = 2
    ARTIST_ALBUM_NR_TITLE = 3
    TITLE = 4
    NR__ARTIST_TITLE = 5


class Structure:

    def __init__(self, folder_struct: FolderStructure,
                 file_struct: FileNameStructure):
        self.folder_struct = folder_struct
        self.file_struct = file_struct
