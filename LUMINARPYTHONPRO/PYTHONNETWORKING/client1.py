import socket

client=socket.socket()

print("connecting...")
client.connect(("localhost",9001))
print("connected")

