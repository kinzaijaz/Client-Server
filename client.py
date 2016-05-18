import socket  # Import socket module
from _thread import *
from Tools.Scripts.treesync import raw_input

s = socket.socket()
host = socket.gethostname()
port = 5182  # Reserve a port for your service.
def receive(d):
    while True:
        data1 = (s.recv(1024)).decode()
        print(str(data1))
        if not data1:
            break

s.connect((host, port))
start_new_thread(receive, (None,))
while True:
    data = raw_input()
    s.send(data)
    start_new_thread(receive, (None,))

s.close  # Close the socket when done
