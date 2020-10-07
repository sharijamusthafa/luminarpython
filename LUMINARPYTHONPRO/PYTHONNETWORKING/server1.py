#package socket
import socket

server=socket.socket()

server.bind(("localhost", 9001))

server.listen(10)
print("waiting for client connection")
client=server.accept()
print("client connected")

print(client)