# based on alpine:3.7
FROM buildbot/buildbot-master:master

# install dev dependencies
RUN apk add build-base python3-dev libffi-dev

# install pillow dependencies
RUN apk add jpeg-dev zlib-dev cairo cairo-dev 

# install openssl dependencies
RUN apk add openssl-dev 

# reinstall pyopenssl (to solve TLS problems with mail notifier)
RUN pip3 uninstall -y pyopenssl
RUN pip3 uninstall -y cryptography
RUN pip3 install pyopenssl

# install additionnal buildbot plugins
RUN pip3 install buildbot-badges
RUN pip3 install buildbot-slack

CMD ["dumb-init", "/usr/src/buildbot/docker/start_buildbot.sh"]