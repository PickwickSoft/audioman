FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN apt install python3-mutagen \
    && pip install pyacoustid \
    && sudo apt-get install ffmpeg \
    && pip install musicbrainzngs \
    && pip install filetype \
    && sudo rm -rf /var/lib/apt/lists/*