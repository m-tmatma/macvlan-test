#!/usr/bin/python3
import socket
import time
import sys

def loop(multicast_index: int):
    MCAST_GROUP = 'ff02::1'
    MCAST_PORT = 12345

    # IPv6 ソケットを作成
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, 1)

    # 使用するインターフェースを設定
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_IF, multicast_index)

    while True:
        message = b"Hello, Multicast World!"
        sock.sendto(message, (MCAST_GROUP, MCAST_PORT))
        print(f'Sent message: {message}')
        time.sleep(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 multicast_sender.py <multicast_index>')
        sys.exit(1)

    multicast_index = int(sys.argv[1])
    loop(multicast_index)
