#--------------------------------------------------------------------------------------------------------
# sudo firewall-cmd --permanent --add-protocol=ipv6-icmp
# sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv6" destination address="ff02::1" accept'
# sudo firewall-cmd --permanent --add-port=12345/udp
# sudo firewall-cmd --reload
#--------------------------------------------------------------------------------------------------------
import socket
import struct
import fcntl

MULTICAST_GROUP = "ff02::1"  # 全ノードマルチキャストアドレス
PORT = 12345

def get_interface_index(interface_name):
    """インターフェース名からインデックスを取得"""
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    return socket.if_nametoindex(interface_name)

def main():
    # IPv6 UDP ソケットを作成
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # すべてのインターフェースでバインド
    sock.bind(("::", PORT))

    # インターフェースを明示的に取得
    interface_index = get_interface_index("enp86s0")  # 使用するインターフェース名を指定（例: eth0）

    # IPv6 マルチキャストグループに参加
    group = socket.inet_pton(socket.AF_INET6, MULTICAST_GROUP)
    mreq = group + struct.pack('@I', interface_index)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

    print(f"Listening for multicast on {MULTICAST_GROUP}:{PORT} (interface enp86s0)")

    while True:
        data, addr = sock.recvfrom(4096)
        print(f"Received from {addr}: {data}")

        # 受信したデータをそのまま送信元に返信
        sock.sendto(data, addr)
        print(f"Replied to {addr}")

if __name__ == "__main__":
    main()
