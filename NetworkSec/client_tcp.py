import socket

target_host = "google.pl"
target_port = 80
banner = "GET / HTTP/1.1\r\nHost: www.google.pl\n\r\n"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET - ipv4, SOCK_STREAM is for TCP

client.connect((target_host, target_port))

client.send(banner.encode())

response = client.recv(4096)

print(response)
