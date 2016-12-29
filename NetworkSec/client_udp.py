import socket

target_host = "127.0.0.1"
target_port = 80
banner = "AAABBBCCC".encode()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# We dont need to use connect - because udp is not connect protocol like tcp

client.sendto(banner, (target_host, target_port))

data, addr = client.recvfrom(4096)

print(data)