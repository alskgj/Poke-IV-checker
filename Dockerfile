FROM debian:jessie

MAINTAINER Max Schrimpf <code@schrimpf.ch>

ENV WORKSPACE_LOCATION="/workspace"
ENV START_SCRIPT="/start.sh"

RUN mkdir $WORKSPACE_LOCATION \
    && chown $IMAGE_USER:$IMAGE_USER $WORKSPACE_LOCATION \
    && apt-get -y update \
    && apt-get install -y python3 \
                          python3-pip \
                          git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && echo "#!/bin/bash" >> $START_SCRIPT \
    && echo "set -e " >> $START_SCRIPT \
    && echo "pip3 install -r /workspace/requirements.txt" >> $START_SCRIPT \
    && echo "python3 /workspace/main.py" >> $START_SCRIPT \
    && chown $IMAGE_USER:$IMAGE_USER $START_SCRIPT \
    && chmod u+x $START_SCRIPT 

VOLUME ["$WORKSPACE_LOCATION"]
WORKDIR /$WORKSPACE_LOCATION

CMD ["/start.sh"]
