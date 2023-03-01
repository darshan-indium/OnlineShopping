//import pandas
import socket

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect(("localhost",4000))

while True:
    data=input("Enter a word: ")
    c.send(bytes(data,"UTF-8"))
    data2=input("To check if substring or not")
    c.send(bytes(data2,"UTF-8"))
    value=c.recv(1024)
    print(value.decode())
