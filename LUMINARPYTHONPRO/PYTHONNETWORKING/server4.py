import socket
import _thread

server = socket.socket()

server.bind(("localhost", 9001))

server.listen(10)

def client_thread(client):
    name = ""
    while True:
        msg = client.recv(1024).decode("ascii")
        command,arguments = msg.split(":")
        if command=='connect':
            name = arguments
        elif command=='message':
            message = arguments
            print("Message from %s: %s" % (name, message))
        elif command=='disconnect':
            print("Disconnecting ", name)
            client.close()
            break
while True:
    client,addr = server.accept()
    print(addr)
    clientthread = _thread.start_new_thread(client_thread, (client,))