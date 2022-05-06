from encodings import utf_8
from http import client, server
import socket
import sys

host = "127.0.0.1"
port = 12346
try:
    soc = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    soc.bind((host, port))
except socket.error as err:
    print("Failed to create socket")
    print("reason: " + str(err))
    sys.exit()

print("socket creation successful")
soc.listen(5)

try:
    while True:
        print("waiting for new connection")
        client_soc, addr = soc.accept()
        print("client connected from " + str(addr))
        while True:
            data = client_soc.recv(1024)
            if not data or data.decode('utf_8') == 'END':
                break
            print("data from client: %s"% data.decode('utf_8'))
            try:
                client_soc.send("hey client".encode('utf-8'))
            except:
                print("couldn't send data, connection closed by client")
        client_soc.close()
except KeyboardInterrupt:
    print("keyboard interrupt")    
soc.close()

