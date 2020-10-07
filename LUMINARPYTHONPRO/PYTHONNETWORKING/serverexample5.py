import socket
import _thread

server = socket.socket()

server.bind(("localhost",9001))

server.listen(10)

clients = {}

def client_thread(client):
    global clients

    name = client.recv(1024).decode("ascii")
    clients[name] = client
    print("name:socket %s:%s" % (name, client))
    while True:
        message = client.recv(1024)
        message = message.decode("ascii")
        to,message = message.split(":")
        if to=="all":
            tomesssage = "%s:%s" % (name, meassage)
            for k,v in clients.items():
                if k!=name:
                 v.sendall(tomessage.encode("asccii"))
        elif to in clients.keys():
            toclient = clients[to]
            tomesssage = "%s:%s" % (name, message)
            toclient.sendall(tomesssage.encode("ascii"))

while True:
    print("[INFO] Waiting For Client")
    client,addr = server.accept()
    print("[INFO] Client Connected")
    print(addr)
    clientthread = _thread.start_new_thread(client_thread,(client,))
