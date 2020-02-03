# tcp client

import socket

req = 'Hello'.encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clnt:
    clnt.connect(('127.0.0.1', 1234))
    print("Sending:", req)
    clnt.send(req)
    rsp = clnt.recv(1024)
    print("Received:", rsp.decode())
