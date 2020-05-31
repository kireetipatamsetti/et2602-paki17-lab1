#usr/bin/python

import sys
import re
import socket

if len(sys.argv) != 3:
    print("Usage: ./chatclient <server-ip>:<server-port> <nickname>")
    sys.exit()
args = str(sys.argv[1]).split(':')
ip = str(args[0])
port = int(args[1])
name = str(sys.argv[2])
client = socket.socket()
client.connect((ip, port))
hello = client.recv(1024).decode('ascii')
print(hello)