#!/bin/sh

docker network create -d macvlan \
  --ipv6 \
  --subnet 2001:db8:100::/64 \
  --gateway 2001:db8:100::1 \
  --subnet=192.168.11.0/24 \
  --gateway=192.168.11.1 \
  -o parent=enp86s0 macvlan
