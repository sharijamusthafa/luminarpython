import socket
import _thread
import base64
import os

server = socket.socket()

server.bind(("localhost",9001))

server.listen(10)

clients = {}

def client_thread(client):
    global clients
    name = client.recv(1024).decode("ascii")
    clients[name] = client
    print(clients)
    print("name:socket %s:%s" % (name, client))
    while True:
        message = client.recv(1024)
        message = message.decode("ascii")
        cm,to,message = message.split(":")
        cmd,mode=cm.split(" ")
        if cmd=="msg":
            if to=="all":
                tomesssage = "msg:%s:%s" % (name, message)
                for k,v in clients.items():
                    if k!=name:
                        v.sendall(tomesssage.encode("ascii"))
            elif to in clients.keys():
                toclient = clients[to]
                tomesssage = "msg:%s:%s" % (name, message)
                toclient.sendall(tomesssage.encode("ascii"))
        else:
            too=cmd
            filename=to
            size=message
            size = int(size)
            print("Size: ", size)
            if not os.path.isdir(("server files/%s send" % (too))):
                os.makedirs(("server files/%s send" % (too)))
            with open("server files/%s send/%s" % (too,filename), 'wb') as f:
                imagearr = client.recv(size)
                imagearrdec = imagearr.decode('ascii')
                base64encoded = ""
                while not "[endoffile]" in imagearrdec:
                    base64encoded += imagearrdec
                    imagearr = client.recv(size)
                    imagearrdec = imagearr.decode('ascii')
                if "[endoffile]" in imagearrdec:
                    imagearrdec = imagearrdec.replace("[endoffile]", "")
                    base64encoded += imagearrdec

                image = base64.b64decode(base64encoded.encode('ascii'))
                f.write(image)
                f.flush()
            with open("server files/%s send/%s" % (too,filename), 'rb') as f:
                image = f.read()
                print("File Size: ", len(image))
                f.close()
                fileb64encoded = base64.b64encode(image)
                fileb64encoded = fileb64encoded.decode('ascii')
                size = len(fileb64encoded)
                print("Base64 Size: ", size)
                if mode == "one":
                    toclient=clients[too]
                    toclient.send(("%s:%s:%d" % (too, filename, size)).encode("ascii"))
                    toclient.send(fileb64encoded.encode('ascii'))
                    toclient.send("[endoffile]".encode('ascii'))
                    print("file send to", too)
                elif mode=="all":
                    for k, v in clients.items():
                        if k != name:
                            toclient = v
                            toclient.send(("%s:%s:%d" % (too, filename, size)).encode("ascii"))
                            toclient.send(fileb64encoded.encode('ascii'))
                            toclient.send("[endoffile]".encode('ascii'))
                            print("file send to", v)



while True:
    print("[INFO] Waiting For Client")
    client,addr = server.accept()
    print("[INFO] Client Connected")
    print(addr)
    clientthread = _thread.start_new_thread(client_thread,(client,))
