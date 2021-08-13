import glob
import filetype


class AudioFileLocator:

    @staticmethod
    def locate_files(root_dir: str, *excluded_dirs: str) -> list:
        """
        Get recursively all audio files starting at the given root_dir
        """
        files = []
        all_files = glob.glob(root_dir + "/**/*.*", recursive=True)
        print(all_files)
        for file in all_files:
            excluded = False
            if str(filetype.guess_mime(file)).startswith("audio/"):
                for dir in excluded_dirs:
                    if file.startswith(dir):
                        excluded = True
                        break
                if not excluded:
                    files.append(file)

        return files
