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
client.sendall(('NICK ' + name).encode('ascii'))
ok = client.recv(1024).decode('ascii')
if re.search('ERROR', ok) or re.search('Error', ok):
    print(ok)
    sys.exit(1)
print(ok)
