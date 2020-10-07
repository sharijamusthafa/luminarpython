import socket

client = socket.socket()

client.connect(("localhost", 9001))
print("connected")
name=input("Enter the name:")
str ="I am "+name
print("sending data")
client.send(str.encode("ascii"))

print("message from server",client.recv(1024).decode("ascii"))



client.close()