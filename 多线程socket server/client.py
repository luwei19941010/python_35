#-*-coding:utf-8-*-
# Author:Lu Wei
import socket

sk=socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    sk.send(b'hello')
    a=sk.recv(1024).decode('utf-8')
    print(a)

