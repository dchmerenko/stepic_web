
import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 2222))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        while True:
            data = conn.recv(1024)
            if not data or data == b"close":
                break
            conn.send(data)
        conn.close()

