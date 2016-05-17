import socket  # Import socket module

from Tools.Scripts.treesync import raw_input

s = socket.socket()
host = socket.gethostname()
port = 5182  # Reserve a port for your service.

s.connect((host, port))
print(s.recv(1024))
while True:
    data = raw_input()
    s.send(data)
    print(s.recv(1024))

s.close  # Close the socket when done
