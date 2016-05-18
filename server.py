'''
    Simple socket server using threads
'''

import socket
import sys
from _thread import *

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5182  # Arbitrary non-privileged port
global conn

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print ('Socket bind complete')

# Start listening on socket
s.listen(10)
print('Socket now listening')

# Function for handling connections. This will be used to create threads
def clientthread(i):
    # Sending message to connected client
    if i%2 ==0:
        conn[i].send(b'Welcome to the server. Type something and hit enter\n')  # send only takes string
    arr = ['Client1', 'Client2']
    # infinite loop so that function do not terminate and thread do not end.
    while True:
        # Receiving from client
        data = (conn[i].recv(1024)).decode()
        if not data:
            break
        print ('Receiving from ' + str(arr[i]) + ': '+ str(data))
        if not i % 2 == 0:
            print('Sending to ' + str(arr[i - 1]))
            data = str(arr[i]) + ': ' + str(data)
            data = data.encode()
            conn[i-1].sendall(data)
        else:
            print('Sending to ' + str(arr[i + 1]))
            data = str(arr[i]) + ': ' + str(data)
            data = data.encode()
            conn[i + 1].sendall(data)

    # came out of loop
    conn[i].close()


conn= [0, 0]
for i in range (0,2):
    # wait to accept a connection - blocking call
    conn[i], addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (i,))

s.close()

