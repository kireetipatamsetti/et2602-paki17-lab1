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


def main():
    print("Chat server started")
    while True:
        r, w, e = select.select(clients, [], [])
        for socket in r:
            if socket == server:
                try:
                    new_client, addr = server.accept()
                    hello = 'Hello 1\n'
                    new_client.sendall(hello.encode('ascii'))
                    clients.append(new_client)
                    clients_in_queue.append(new_client)
                    print(clients_in_queue)
                except:
                    continue
            elif socket in clients_in_queue:
                try:
                    name_load = socket.recv(1024).decode('ascii')
                    if name_load:
                        received = re.search(r'NICK\s(\S*)', name_load)
                        name = str(received.group(1))
                        if len(name) > 12:
                            error_load = 'ERROR nickname should be less than 13 characters'
                            socket.sendall(error_load.encode('ascii'))
                        elif (re.search(r'!', name) or re.search(r'@', name) or re.search(r'#', name) or re.search(
                                r'\$', name) or re.search(r'%', name) or re.search(r'\*', name) or re.search(r'\^',
                                                                                                             name)):
                            error_load = "ERROR shouldn't use special characters in the name!"
                            socket.sendall(error_load.encode('ascii'))
                        elif received:
                            print("sending ok!")
                            ok_load = 'OK' + '\n'
                            socket.sendall(ok_load.encode('ascii'))
                            permanent_clients[socket] = name
                            clients_in_queue.remove(socket)
                        else:
                            if name_load[:3] == 'MSG':
                                error_load = "ERROR no nick set"
                                socket.sendall(error_load.encode('ascii'))
                            elif name_load[-4:] == 'NICK':
                                error_load = "ERROR malformed command"
                                socket.sendall(error_load.encode('ascii'))
                            else:
                                error_load = "ERROR malformed command"
                                socket.sendall(error_load.encode('ascii'))
                    else:
                        socket.close()
                        clients.remove(socket)
                        clients_in_queue.remove(socket)
                except Exception as e:
                    print(e)
                    continue
            elif socket in permanent_clients.keys():
                try:
                    message = socket.recv(1024).decode('ascii')
                    if message:
                        received = re.search(r'MSG\s', message)
                        if len(message) > 259:
                            error_load = "ERROR Message shouldn't exceed 256 characters"
                            socket.sendall(error_load.encode('ascii'))
                        elif received:
                            message_load = 'MSG ' + str(permanent_clients[socket]) + ': ' + message[4:]
                            broadcast(message_load, socket)
                        else:
                            socket.sendall("ERROR malformed command".encode('ascii'))
                    else:
                        socket.close()
                        clients.remove(socket)
                        del permanent_clients[socket]
                except:
                    continue
            else:
                pass
    server.close()


if __name__ == '__main__':
    main()
