#!/usr/bin/python3

import sys
from mutagen import File

for file in sys.argv[1:]:
    file = File(file)
    file.delete()
    file.save()
