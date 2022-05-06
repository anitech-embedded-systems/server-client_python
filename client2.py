from encodings import utf_8
from http import client
import socket

host = "127.0.0.1"
port = 12346

payload = "hey server from client 2"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

try:
    while True:
        client_socket.send(payload.encode('utf_8'))
        data = client_socket.recv(1024)
        print(str(data))
        more = raw_input("want to send more data to server ")
        print(more)
        if more.lower() == 'y':
            payload = raw_input("enter payload")
        else:
            break
    
except KeyboardInterrupt:
    print("exited by user")
client_socket.close()
