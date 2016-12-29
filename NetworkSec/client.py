import socket

target_host = "www.google.com"
target_port = 80
banner = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(banner.encode())

response = client.recv(4096)

print(response)