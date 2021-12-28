from audioman.fingerprint.identifier import AudioFileIdentifier
from audioman.locator.audio_file_locator import AudioFileLocator
from audioman.lookup.metadata_lookup import MetadataLookup
from audioman.parser.metadata_parser import MetadataParser
from audioman.metadata.tagger import AudioTagger
from audioman.files.structure import Structure, FolderStructure, FileNameStructure
from audioman.files.restructure import FileRestructurer
from audioman.cli import TerminalAlbumChooser

files = AudioFileLocator(".", ()).locate_files()
print(files)

if len(files) == 0:
    exit(0)

identifier = AudioFileIdentifier(files[0])
id = identifier.identify
print('http://musicbrainz.org/recording/%s' % id)

data = MetadataLookup.lookup(str(id))
metadata = MetadataParser(data, TerminalAlbumChooser(files[0])).parse_metadata()
print(metadata.artist, metadata.rating, metadata.title, sep=", ")

tagger = AudioTagger.get_tagger(files[0])
tagger.tag(metadata)
tagger.save()

FileRestructurer("./", Structure(FolderStructure.ARTIST_ALBUM,
                                 FileNameStructure.ARTIST_TITLE)).move(files[0], metadata)
