#!/usr/bin/python3
from audioman.fingerprint.identifier import AudioFileIdentifier
from audioman.locator.audio_file_locator import AudioFileLocator
from audioman.lookup.metadata import MetadataLookup

files = AudioFileLocator.locate_files(".")
print(files)
identifier = AudioFileIdentifier(files[0])
id = identifier.identify()
print('http://musicbrainz.org/recording/%s' % id)
metadata = MetadataLookup.lookup(id)
print(metadata)