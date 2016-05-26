'''
    Simple socket server using threads
'''

import socket
import sys
from _thread import *

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5162  # Arbitrary non-privileged port
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
s.listen(20)
print('Socket now listening')
# Function for handling connections. This will be used to create threads
def clientthread(i):
    # infinite loop so that function do not terminate and thread do not end.
    while True:
        # Receiving from client
        data = (conn.recv(1024)).decode()
        if not data:
            break
        print ('Receiving from ' + str(client[i]) + ': '+ str(data))
        if conn==arr[0]['conn']:
            print('Sending to ' + str(client[i]))
            data = str(client[i]) + ': ' + str(data)
            data = data.encode()
            conn.sendall(data)
        elif conn==arr[1]['conn']:
            print('Sending to ' + str(client[i]))
            data = str(client[i]) + ': ' + str(data)
            data = data.encode()
            conn.sendall(data)
    # came out of loop
    conn[i].close()

def onlineusers(arr):
    for i in range(0, len(arr)):
        d = str(arr[i]['name'] + "is online")
        d = d.encode()
        arr[i]['conn'].send(d)

client=['Client1','Client2','Client3','Client4','Client5','Client6','Client7','Client8','Client9','Client10','Client11','Client12','Client13','Client14','Client15','Client16','Client17','Client18','Client19','Client20']
dict={}
arr=[]

for i in range (30):
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    dict['conn']=conn
    dict['name']=client[i]
    dict['address']=addr[1]
    arr.append(dict)
    print('Connected with ' + addr[0] + ':' + str(addr[1])+ ':' + client[i])
    onlineusers(arr)
    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (i,))

s.close()

