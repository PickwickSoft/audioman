FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN apt install python3-mutagen \
    && pip install pyacoustid \
    && pip install musicbrainzngs \
    && sudo rm -rf /var/lib/apt/lists/*