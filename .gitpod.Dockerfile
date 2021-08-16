FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN sudo apt-get update \
    && sudo apt-get install -y python3-mutagen \
    && sudo apt-get install -y ffmpeg \
    && pip install musicbrainzngs \
    && pip install pyacoustid \
    && pip install filetype \
    && sudo rm -rf /var/lib/apt/lists/*
