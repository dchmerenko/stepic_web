# tcp server

import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.bind(('127.0.0.1', 1234))
    srv.listen(10)
    while True:
        conn, addr = srv.accept()
        print("Conneted by", addr)
        while True:
            data = conn.recv(1024)
            print("Recieved:", data)
            if not data:
                break
            print("Sending:", data)
            conn.send(data)
        conn.close()
