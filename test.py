#!/usr/bin/python3
from audioman.fingerprint.identifier import AudioFileIdentifier
from audioman.locator.audio_file_locator import AudioFileLocator

files = AudioFileLocator.locate_files(".")
print(files)
identifier = AudioFileIdentifier(files[0])
id = identifier.identify()
print('http://musicbrainz.org/recording/%s' % id)
