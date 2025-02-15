import socket
import time

MCAST_GROUP = 'ff02::1'
MCAST_PORT = 12345
INTERFACE_NAME = 'enp86s0'  # 使用するインターフェースを指定（例: eth0, wlan0 など）

# IPv6 ソケットを作成
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, 1)

# 使用するインターフェースを設定
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_IF, socket.if_nametoindex(INTERFACE_NAME))

while True:
    message = b"Hello, Multicast World!"
    sock.sendto(message, (MCAST_GROUP, MCAST_PORT))
    print(f'Sent message: {message}')
    time.sleep(1)
