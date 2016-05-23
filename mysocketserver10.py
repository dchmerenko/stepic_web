import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 1234))
sock.listen(10)

print("Server is listening ...")

while True:
    conn, addr = sock.accept()
    print('Server connected with client:', addr)
    pid = os.fork()
    if pid:  # pid != 0 -> in parent process
        continue
    else:
        while True:
            data = conn.recv(1024)
            print("Process %s received from client: %s" % (os.getpid(), data.decode()))
            if data == b'q' or not data:
                print("Stop simbol \"%s\" has received from server" % data.decode())
                break
            rsp = data.upper()
            conn.send(rsp)
            print("Sended to client:", rsp.decode())

        conn.shutdown(socket.SHUT_RDWR)
        conn.close()
        print("Connection has closed")
        os._exit(0)





