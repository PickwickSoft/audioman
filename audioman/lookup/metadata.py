import musicbrainzngs
import audioman


class MetadataLookup:

    @staticmethod
    def lookup(recording_id: str) -> dict:
        musicbrainzngs.set_useragent(
            audioman.__app__, audioman.__version__, audioman.__contact__)
        return musicbrainzngs.get_recording_by_id(id)
