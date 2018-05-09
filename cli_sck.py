import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b"11",('21.12.11.31',7000))
client.close()