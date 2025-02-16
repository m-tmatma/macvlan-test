# docker setting

```
$ cat /etc/docker/daemon.json
{
  "ipv6": true,
  "fixed-cidr-v6": "fd00:dead:beef::/64"
}
```

```
sudo systemctl restart docker
```

```
sudo ip link add macvlan-shim link enp86s0 type macvlan mode bridge
sudo ip addr add fd00::1/64 dev macvlan-shim
sudo ip link set macvlan-shim up
```

```
./network.sh
```

```
$ ip addr show
    ...
422: macvlan-shim@enp86s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    ...
```

```
./run.sh -d
./run.sh -d
./run.sh -d
```

```
./multicast_sender.py 422
```




