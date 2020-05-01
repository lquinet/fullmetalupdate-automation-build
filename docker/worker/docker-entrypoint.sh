#!/bin/bash

set -e

if [ -z "$BITBUCKET_USERNAME" ] || [ -z "$BITBUCKET_PASSWORD" ]; then
        echo '$BITBUCKET_USERNAME or $BITBUCKET_PASSWORD does not exist'
		exit 1
fi

git clone https://$BITBUCKET_USERNAME:$BITBUCKET_PASSWORD@bitbucket.org/adeneo-embedded/farm-core.git

cd farm-core/ && ./install.sh

cd /buildbot

/usr/bin/dumb-init twistd --pidfile= -ny buildbot.tac