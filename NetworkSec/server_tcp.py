"""
TCP three way handshake

SYN
SYN-ACK
ACK
FIN-ACK
ACK
"""
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999


def handle_client(client_socket):
    """
    Fuction print all info sent from client.
    Function should be thread.

    Args:
        client_socket:

    Returns:

    """
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)
    client_socket.send("ACK!".encode())

    client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

# listen max to 5 connections
server.listen(5)

print("[*] Listening on the port %s:%d" % (bind_ip, bind_port))

while True:
    # Main loop waiting for connection

    # client is socket of connection
    # addr is connection data
    client, addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

    # creating of the thread for connection (data receiving)

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()