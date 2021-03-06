# based on ubuntu:18.04
FROM buildbot/buildbot-worker:master

# Switch to root to be able to install stuff
USER root

# This will make apt-get install without question
ARG DEBIAN_FRONTEND=noninteractive

# Install packages for FMU
RUN apt-get -yqq update \
    && apt-get -yqq install \
        python3 \
        python3-pip \
        curl \
        git \
        golang-docker-credential-helpers 

# Install docker
WORKDIR /home/
RUN curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh get-docker.sh

# Allow buildbot user to use docker
RUN groupadd docker \
    ; usermod -aG docker buildbot

# Dependencies for farm-core
RUN apt-get -yqq install locales telnet 
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

# Switch to root to have all permissions (need to use dd command, etc.)
USER root
WORKDIR /buildbot

# Set-up the entry point of the container
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]