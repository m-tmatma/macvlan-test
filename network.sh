#!/bin/sh

docker network create -d macvlan \
  --ipv6 \
  --subnet 2001:db8:100::/64 \
  --gateway 2001:db8:100::1 \
  -o parent=enp86s0 macvlan
