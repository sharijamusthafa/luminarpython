import socket
import _thread

server = socket.socket()

server.bind(("localhost", 1004))

server.listen(10)


def client_thread(client):
    while True:
        data = client.recv(1024)
        print(data.decode("ascii"))

while True:
    name=" "
    while True:
        msg=client.recv(1024)
        



    clientthread = _thread.start_new_thread(client_thread, (client,))