import socket  # Import socket module
from _thread import *

s = socket.socket()
host = socket.gethostname()
port = 5182  # Reserve a port for your service.

def receive(para):
    while True:
        data1 = (s.recv(1024)).decode()
        print(str(data1))
        if not data1:
            break
def sends():
    while True:
        data = input()
        s.send(str(data).encode())

s.connect((host, port))
start_new_thread(receive, (None,))
sends()
s.close  # Close the socket when done

