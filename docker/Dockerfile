FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get autoremove --purge -y \
 && apt-get install -y \
     gawk wget git diffstat unzip texinfo gcc-multilib \
     build-essential python3 python3-pip python3-pexpect \
     autoconf libtool git \
     coreutils \
     rsync \
     sudo \
     locales \
     iproute2 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY multicast_responder.py .
CMD ["python3", "multicast_responder.py"]
