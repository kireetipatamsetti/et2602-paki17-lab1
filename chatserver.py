import sys
import re
import socket

if len(sys.argv) != 2:
    print("Usage: ./chatserver <ip>:<port>")
    sys.exit(1)
args = str(sys.argv[1]).split(':')
ip = str(args[0])
port = int(args[1])

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((ip, port))
server.listen(100)
clients = [server]
clients_in_queue = []
permanent_clients = {}


def broadcast(message, client):
    for socket in permanent_clients.keys():
        if socket != client:
            try:
                print("Broadcasting!")
                socket.sendall(message.encode('ascii'))
            except:
                socket.close()
                del permanent_clients[socket]
                clients.remove(socket)


