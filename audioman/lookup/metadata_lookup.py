import musicbrainzngs as mb
import audioman


class MetadataLookup:

    @staticmethod
    async def lookup(recording_id: str) -> dict:
        mb.set_useragent(
            audioman.__app__, audioman.__version__, audioman.__contact__)
        return mb.get_recording_by_id(recording_id, audioman.includes)
