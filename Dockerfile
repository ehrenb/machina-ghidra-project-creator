FROM behren/machina-base-ghidra:latest

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

COPY GhidraProjectCreator.json /schemas/

COPY src /machina/src