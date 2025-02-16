#!/bin/sh

docker run  $@ \
 --network macvlan \
 --cap-add=NET_ADMIN \
 macvlan-test

