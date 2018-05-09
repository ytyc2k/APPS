import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 7000))
sock.listen(5)
while True:
    connection,address = sock.accept()
    try:
        connection.settimeout(5)
        buf = connection.recv(1024)
        print(buf)
        if buf == b"11":
            connection.send('welcome to server!')
            print("good")
        else:
            connection.send('please go out!')
    except socket.timeout:
        print('time out')
    connection.close()