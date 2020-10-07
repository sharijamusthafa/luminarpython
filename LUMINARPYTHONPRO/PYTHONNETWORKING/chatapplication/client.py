import socket
import base64
import _thread
import os

client = socket.socket()

client.connect(("localhost", 9001))

clientname = input(">> Enter Name: ")

client.sendall(clientname.encode("ascii"))

def client_thread(client):
    while True:
        message = client.recv(1024)
        message = message.decode("ascii")
        cmd,fromname,message = message.split(":")
        if cmd=="msg":
            print("New Message From: %s\nMessage: %s" % (fromname,message))
        else:
            too = cmd
            filename = fromname
            size = message
            size = int(size)
            print("Size: ", size)
            if not os.path.isdir(("%s recieved" % (clientname))):
                os.makedirs(("%s recieved" % (clientname)))
            with open("%s recieved/%s" % (clientname, filename), 'wb') as f:
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
            print(">> file recieved")

clientthread = _thread.start_new_thread(client_thread,(client,))

while True:
    clnt=input("1.send message to another client\n2.send message to all\n3.send file to another client \n>> ")
    if not clnt=="3":
        if clnt=="1":
            toclient = input(">> Enter Client Name: ")
            message = input(">> Enter Message: ")
        elif clnt=="2":
            toclient="all"
            message = input(">> Enter Message: ")
        else:
            clnt = input("1.send message to another client\n2.send message to all \n3.send file  \n>> ")
        client.sendall(("msg:%s:%s" % (toclient,message)).encode("ascii"))
    elif clnt=="3":
        mode=input("1.Send to one client\n2.Send to all client\n>>")
        if mode=="1":
            filename=input(">> enter file name : ")
            to=input(">> enter recipient name : ")
            with open(filename, 'rb') as f:
                image = f.read()
                print(">> File Size: ", len(image))
                f.close()
                fileb64encoded = base64.b64encode(image)
                fileb64encoded = fileb64encoded.decode('ascii')
                size = len(fileb64encoded)
                print(">> Base64 Size: ", size)
                client.send(("%s one:%s:%d" % (to,filename, size)).encode("ascii"))
                client.send(fileb64encoded.encode('ascii'))
                client.send("[endoffile]".encode('ascii'))
                print("\n>> file send to",to,"\n")
        elif mode=="2":
            filename = input(">> enter file name : ")
            to = "all"
            with open(filename, 'rb') as f:
                image = f.read()
                print(">> File Size: ", len(image))
                f.close()
                fileb64encoded = base64.b64encode(image)
                fileb64encoded = fileb64encoded.decode('ascii')
                size = len(fileb64encoded)
                print(">> Base64 Size: ", size)
                client.send(("%s all:%s:%d" % (to, filename, size)).encode("ascii"))
                client.send(fileb64encoded.encode('ascii'))
                client.send("[endoffile]".encode('ascii'))
                print("\n>> file send to", to, "\n")
