from encodings import utf_8
import socket
from _thread import *
from threading import Thread

host = '127.0.0.1'
port = 12346
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
thread_count = 0

try:
    server_socket.bind((host, port))
    print("waiting for connection")
    server_socket.listen(2)
except socket.error as err:
    print(str(err))

def client_thread(connection):
    connection.send("Welcome to the server".encode('utf_8'))
    try:
        while True:
            data = connection.recv(1024)
            print(data)
            reply = "hello from server" + data.encode('utf-8')
            if not data:
                break
            connection.send(reply.encode('utf-8'))
    except Exception as err:
        print("reset by peer, " + str(err))
        
    connection.close()
try:
    while True:
        client, addr = server_socket.accept()
        print("connected to ", str(addr))
        start_new_thread(client_thread, (client,))
        thread_count += 1
        print("thread count: ", str(thread_count))
        
except KeyboardInterrupt:
    print("keyboard interrupt")
server_socket.close() 

