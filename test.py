#!/usr/bin/python3
from audioman.fingerprint.identifier import AudioFileIdentifier
from audioman.locator.audio_file_locator import AudioFileLocator
from audioman.lookup.metadata_lookup import MetadataLookup
from audioman.parser.metadata_parser import MetadataParser
from audioman.metadata.tagger import AudioTagger
files = AudioFileLocator.locate_files(".", "test")
print(files)
identifier = AudioFileIdentifier(files[0])
id = identifier.identify()
print('http://musicbrainz.org/recording/%s' % id)
data = MetadataLookup.lookup(str(id))
# print(data)
metadata = MetadataParser(data).parse_metadata()
print(metadata.artist, metadata.rating, metadata.title, sep=", ")
tagger = AudioTagger.get_tagger(files[0])
tagger.tag(metadata)
tagger.save()
