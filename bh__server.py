#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:53:44 2019

@author: irinasm
"""

###   Server   ###
# Receive the file

#from socket import *
#import base64

#sock = socket.socket() #наш сокет ???

#my_to_file = "my_file.ged"  # imya fajla???

#HOST = ""    #оставим строку пустой, чтобы наш сервер был доступен для всех интерфейсов
#PORT = 9090  #порт возьмем любой от нуля до 65535.


#s = socket(AF_INET, SOCK_STREAM)

#s.bind((HOST, PORT))  #свяжем наш сокет с данными хостом и портом
#s.listen(1)           #запустим для данного сокета режим прослушивания

#conn, addr = s.accept() #можем принять подключение с помощью метода accept,
                        #который возвращает кортеж с двумя элементами:
                        #новый сокет и адрес клиента. 
                        #Именно этот сокет и будет использоваться для приема и посылке клиенту данных.

#print ("Connecting by", addr)

#file = open("my_file.ged", addr)  # imya fajla???
#    file = conn.recv(str)
#    buff = str.write(1024)
 #   str = base64.b64decode(buff)
#    if not data:
#        break

import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

#while True:
 #   data = conn.recv(1024)
  #  if not data:
    #    break
   # conn.send(data.upper())

conn.close()