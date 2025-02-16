#!/usr/bin/python3
import socket
import time
import sys
import select

def get_interface_index(interface_name: str) -> int:
    return socket.if_nametoindex(interface_name)

def loop(multicast_index: int, loop_count: int = 0):
    MCAST_GROUP = 'ff02::1'
    MCAST_PORT = 12345

    # IPv6 ソケットを作成
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, 1)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_IF, multicast_index)

    # 受信用の設定
    sock.bind(('::', MCAST_PORT))

    print(f"loop_count: {loop_count}")
    while True:
        if loop_count >= 0:
            loop_count -= 1
            if loop_count < 0:
                break

        # コマンドの送信
        message = b"Hello, Multicast World!"
        sock.sendto(message, (MCAST_GROUP, MCAST_PORT))
        print(f'Sent message: {message}')

        # 1秒間応答を待機
        timeout = time.time() + 1.0
        while time.time() < timeout:
            # select を使って待機
            ready = select.select([sock], [], [], 0.1)
            if ready[0]:
                try:
                    data, addr = sock.recvfrom(4096)
                    print(f"Received from {addr}: {data.decode()}")
                except socket.error as e:
                    print(f"Error receiving data: {e}")

        print("Waiting for next command...")
        time.sleep(1)

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('Usage: python3 multicast_sender.py <multicast_index>')
        print('Usage: python3 multicast_sender.py <multicast_index> <loop_count>')
        sys.exit(1)

    try:
        multicast_index = int(sys.argv[1])
    except ValueError:
        multicast_index = get_interface_index(sys.argv[1])

    loop_count = int(sys.argv[2]) if len(sys.argv) == 3 else -1
    loop(multicast_index, loop_count)
