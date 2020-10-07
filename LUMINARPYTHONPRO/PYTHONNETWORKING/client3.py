import socket

client = socket.socket()

client.connect(("localhost", 9001))
print("connected")
num=input("Enter the first number:")
secondnum=input("Enter the second number:")

print("sending addition")
client.send(num.encode("ascii"))
client.send(secondnum.encode("ascii"))
print("addition result:",client.recv(1024).decode("ascii"))
print("subtraction result:",client.recv(1024).decode("ascii"))
print("multiplication result:",client.recv(1024).decode("ascii"))
client.close()