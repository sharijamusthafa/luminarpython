import socket

server = socket.socket()

server.bind(("localhost",9001))

server.listen(10)

while True:
    print("Waiting For client..")
    client, addr = server.accept()
    print("Client connected ", addr)
    str1 = client.recv(2024)

    msg = str1.decode('ascii')

    arr=msg.split(" ")

    print("Message from client ", msg)

    str2 = "Hello"+arr[-1]
    client.send(str2.encode('ascii'))

    client.close()
    print("Client disconnected!")

