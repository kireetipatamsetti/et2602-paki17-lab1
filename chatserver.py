
import sys
import re
import socket
if len(sys.argv) != 2:
    print("Usage: ./chatserver <ip>:<port>")
    sys.exit(1)
args = str(sys.argv[1]).split(':')
ip = str(args[0])
port = int(args[1])

