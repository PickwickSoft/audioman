FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN apt-get install -y python3-mutagen \
    && apt-get -y install ffmpeg \
    && pip install musicbrainzngs \
    && pip install pyacoustid \
    && pip install filetype \
    && sudo rm -rf /var/lib/apt/lists/*
