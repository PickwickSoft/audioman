import glob
import mimetypes
import os
import magic


class AudioFileLocator:

    @staticmethod
    def locate_files(root_dir: str, *excluded_dirs: str) -> list:
        """
        Get recursively all audio files starting at the given root_dir
        """
        files = []
        all_files = glob.glob(root_dir + "/**/*.*", recursive=True)
        for file in all_files:
            excluded = False
            if str(magic.Magic(mime=True).from_file(file)).startswith("audio/"):
                for dir in excluded_dirs:
                    if dir != "" and dir is not None and os.path.abspath(file).startswith(os.path.abspath(dir)):
                        excluded = True
                        break
                if not excluded:
                    files.append(os.path.abspath(file))

        return files
