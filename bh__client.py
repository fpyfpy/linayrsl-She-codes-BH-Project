#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:51:55 2019

@author: irinasm
"""
    
###   Client   ###
# Send file to server

from socket import *
import base64

my_file = "hello.docx"
#my_file = 'user.json'

HOST = "localhost"  #my local server address 
PORT = 4567      #free port in my computer
s = socket(AF_INET, SOCK_STREAM)  #AddressFamily
s.connect((HOST, PORT))
print ("Client running on %s port %s" % (HOST, PORT))

with open("my_file", "rb") as my_reading_file:
    print ("The file %s is open now", my_file)  #potom ubrat'
    
    while True:
        buffer = my_reading_file.read(1024)  #read 1024 bytes
        if len(buffer) == 0:
            break
        temp_string = base64.b64encode(buffer)
        print (temp_string) #???
        
        s.send(temp_string)
        print ("Data has been sent")
    
s.close()    
print ("Connection is closed")    