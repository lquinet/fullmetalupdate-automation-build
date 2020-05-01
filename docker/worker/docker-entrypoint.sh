#!/bin/bash

set -e

git clone https://$BITBUCKET_USERNAME:$BITBUCKET_PASSWORD@bitbucket.org/adeneo-embedded/farm-core.git

cd farm-core/ && ./install.sh

cd /buildbot

/usr/bin/dumb-init twistd --pidfile= -ny buildbot.tac