import glob
import os

import magic


class AudioFileLocator:

    def __init__(self, root_dir: str, *excluded_dirs):
        self.root = root_dir
        self.excluded_items = [os.path.abspath(i) for i in list(excluded_dirs[0])]

    def locate_files(self) -> list:
        """
        Get recursively all audio files starting at the given root_dir
        """
        files = []
        all_files = self.__get_files_recursive()
        for file in all_files:
            excluded = False
            if self.__is_audio_file(file):
                for dir in self.excluded_items:
                    if os.path.abspath(file).startswith(dir):
                        excluded = True
                        break
                if not excluded:
                    files.append(os.path.abspath(file))

        return files

    def __get_files_recursive(self):
        result = glob.glob(f"{self.root}/**/*.*", recursive=True)
        return [element for element in result if os.path.isfile(element)]

    @staticmethod
    def __is_audio_file(file):
        return str(magic.Magic(mime=True).from_file(file)).startswith("audio/")
