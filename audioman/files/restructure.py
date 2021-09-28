import shutil
import os
from audioman.files.structure import Structure, FolderStructure, FileNameStructure
from audioman.metadata.metadata import Metadata


class FileRestructurer:

    def __init__(self, root: str, struct: Structure):
        self.root = root
        self.struct = struct
        self.meta = None

    def move(self, file: str, meta: Metadata):
        self.meta = meta
        self.__create_dir_structure()
        shutil.move(file, os.path.join(
            self.root, self.__create_file_name_structure() + "." + file.split(".")[-1]))

    def __create_dir_structure(self):
        dir_path = self.struct.folder_struct.name.replace(
            "artist", self.meta.artist).replace("album", self.meta.album)
        dir_path = self.root + dir_path
        dirs = dir_path.split("/")
        root = self.root
        for dir in dirs:
            path = os.path.join(root, dir)
            if not os.path.isdir(path):
                os.mkdir(path)
            root = path
        self.root = root

    def __create_file_name_structure(self):
        # Special Case:
        if self.struct.file_struct == FileNameStructure.ARTIST_ALBUM_NUMBER_TITLE:
            # Artist (Album) - Number - Title
            return "{0} ({1}) - {2} - {3}".format(
                self.meta.artist, self.meta.album, "00", self.meta.title
            )

        else:
            return (
                self.struct.file_struct.name.lower()
                .replace("nr", "00")
                .replace("artist", self.meta.artist)
                .replace("title", self.meta.title)
            )
