FROM debian:jessie

MAINTAINER Max Schrimpf <code@schrimpf.ch>

ENV IMAGE_USER="pokerater"

ENV WORKSPACE_LOCATION="/workspace"
ENV START_SCRIPT="/start.sh"


RUN groupadd $IMAGE_USER \
    && useradd $IMAGE_USER -s /bin/bash -m -g $IMAGE_USER -G $IMAGE_USER \
    && mkdir $WORKSPACE_LOCATION \
    && chown $IMAGE_USER:$IMAGE_USER $WORKSPACE_LOCATION \
    && apt-get -y update \
    && apt-get install -y python3 \
                          python3-pip \
                          git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

USER $IMAGE_USER

VOLUME ["$WORKSPACE_LOCATION"]
WORKDIR /$WORKSPACE_LOCATION

CMD ["python3", "/workspace/main.py"]
