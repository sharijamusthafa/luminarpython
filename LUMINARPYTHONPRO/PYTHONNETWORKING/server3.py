import socket

server =socket.socket()

server.bind(("localhost", 9001))

server.listen(10)

while True:
    print("WAITING FOR CLIENT...")
    client, addr=server.accept()
    print("client connect",addr)
    str1 = client.recv(2024)
    str2 = client.recv(1024)
    num1 = str1.decode('ascii')
    num2 = str2.decode('ascii')

    print("first number from client ", num1)
    print("second number from client", num2)

    str3 = int(num1) + int(num2)
    str4 = int(num1) - int(num2)
    str5 = int(num1) / int(num2)
    client.send(str(str3).encode('ascii'))
    client.send(str(str4).encode('ascii'))
    client.send(str(str5).encode('ascii'))
    client.close()
    print("Client disconnected!")