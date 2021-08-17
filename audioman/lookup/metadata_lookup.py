import musicbrainzngs as mb
import audioman


class MetadataLookup:

    @staticmethod
    def lookup(recording_id: str) -> dict:
        mb.set_useragent(
            audioman.__app__, audioman.__version__, audioman.__contact__)
        data = mb.get_recording_by_id(recording_id, audioman.includes)
        return data
