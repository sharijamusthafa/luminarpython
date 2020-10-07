import socket
import time


client = socket.socket()
client.connect(("localhost", 9001))
while True:
    name=input("enter a name:")
    msgg=input("enter message..")

    str1="connect:"+name
    str2="message:"+msgg
    str3="disconnect:"+name

    client.send(str1.encode("ascii"))
    client.send(str2.encode("ascii"))
    client.send(str3.encode("ascii"))
    client.close()
