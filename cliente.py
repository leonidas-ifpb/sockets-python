#!/usr/bin/env python3
import socket

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 40000           # Porta que o Servidor esta

serv = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)
msg = 'Oi Mundo Socket!'
sock.send(str.encode(msg))
msg = sock.recv(1024)
if msg:
    msg = msg.decode()
    print('Recebi:', msg)
sock.close()
