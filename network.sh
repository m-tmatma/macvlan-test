#!/bin/sh

# ネットワークインターフェース名を検出
if ip addr show dev enp86s0 >/dev/null 2>&1; then
    INTERFACE="enp86s0"
elif ip addr show dev eth0 >/dev/null 2>&1; then
    INTERFACE="eth0"
else
    echo "エラー: 必要なネットワークインターフェースが見つかりません"
    exit 1
fi

docker network create -d macvlan \
  --ipv6 \
  --subnet 2001:db8:100::/64 \
  --gateway 2001:db8:100::1 \
  -o parent=$INTERFACE macvlan

sudo ip link add macvlan-shim link $INTERFACE type macvlan mode bridge
sudo ip addr add fd00::1/64 dev macvlan-shim
sudo ip link set macvlan-shim up
