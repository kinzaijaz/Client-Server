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
s.listen(10)
print('Socket now listening')

arr=[]
# Function for handling connections. This will be used to create threads
def clientthread(conn):
    # infinite loop so that function do not terminate and thread do not end.
    conn.send(str('Enter name you want to chat with: ').encode())
    while True:
        datacome=(conn.recv(1024)).decode()
        if datacome == "Q" or datacome == "q":
            a = 0
            for a in range(len(arr)):
                if conn == arr[a]['conn']:
                    arr[a]['conn'].send(str('user is now offline').encode())
                    arr[a]['conn'].close()
                    break
        else:
            receiver = None
            sender = " "
            for a in range(len(arr)):
                if (datacome == arr[a]['name']):
                    receiver = arr[a]
                    break
            for a in range(len(arr)):
                if (conn == arr[a]['conn']):
                    sender = arr[a]['name']
            data = (conn.recv(1024)).decode()
            if receiver != None:
                receiver['conn'].send(str(sender+ ': ' + data).encode())
    conn.close()

def newConnectedUsers(dict):
    j = len(arr)
    while j:
        j= j-1
        data2 = str(dict['name'] + ' is now online').encode()
        arr[j]['conn'].send(data2)
    return

i=0
while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    # shows already Connected users with server to newly connected
    k = len(arr)
    while k:
        k = k - 1
        data1 = str(arr[k]['name'] + ' is online\n').encode()
        conn.send(data1)

    dict={}
    dict['conn']=conn
    dict['address']=addr

    # ask new connected user name
    conn.send(str('Enter you name: ').encode())
    dict['name']= (conn.recv(1024)).decode()

    # shows new connected user to all other users
    newConnectedUsers(dict)
    arr.append(dict)

    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn,))
    i = i+1
s.close()

