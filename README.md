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
