FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN sudo apt-get update \
    && sudo apt-get install -y python3-mutagen \
    && sudo apt-get install -y ffmpeg \
    && pip3 install musicbrainzngs \
    && pip3 install pyacoustid \
    && pip3 install python-magic==0.4.24 \
    && pip3 install InquirerPy \
    && pip3 install typer[all] \
    && sudo rm -rf /var/lib/apt/lists/*
