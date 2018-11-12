#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port =  7331

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024)
print(data)

while (1):
    word = ""
    hash = ""
    index = 0
    cmd = data.strip().split()
    index = cmd.index("of")
    word = cmd[index + 1]
    if "sha512" in cmd:
        hash = hashlib.sha512(word).hexdigest()
    elif "sha384" in cmd:
        hash = hashlib.sha384(word).hexdigest()
    elif "sha256" in cmd:
        hash = hashlib.sha256(word).hexdigest()
    elif "sha224" in cmd:
        hash = hashlib.sha224(word).hexdigest()
    elif "sha1" in cmd:
        hash = hashlib.sha1(word).hexdigest()
    elif "md5" in cmd:
        hash = hashlib.md5(word).hexdigest()
    else:
        print("Invalid command" + "\n")
    print("Sending " + hash + "\n")
    s.send(hash + "\n")
    data =  s.recv(1024)
    print(data)

# close the connection
s.close()
