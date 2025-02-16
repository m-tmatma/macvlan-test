#!/bin/sh

docker run -d \
 --network macvlan \
 --cap-add=NET_ADMIN \
 macvlan-test
