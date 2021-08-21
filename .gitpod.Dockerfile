FROM gitpod/workspace-full

# Install custom tools, runtime, etc.
RUN sudo apt-get update \
    && sudo apt-get install -y python3-mutagen \
    &&  sudo apt-get install -y libchromaprint-tools \
    && pip install musicbrainzngs \
    && pip install pyacoustid \
    && pip install python-magic==0.4.24 \
    && pip install PyInquirer \
    && sudo rm -rf /var/lib/apt/lists/*
