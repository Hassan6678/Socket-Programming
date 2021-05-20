from socket import *

serverPort = 12000

'''
Create a socket
socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
'''
serverSocket = socket(family=AF_INET,type=SOCK_STREAM)

# Bind, so server informs operating system that it's going to use given IP and port
serverSocket.bind(('', serverPort))

# This makes server listen to new connections
serverSocket.listen(1)

print ('The server is ready to receive')

while 1:
    '''
     Accept new connection
     That gives us new socket - client/connection socket, connected to this given client only, it's unique for that client
     The other returned object is ip/port set
    '''
    connectionSocket, addr = serverSocket.accept()
    # Recevied message
    sentence = connectionSocket.recv(1024)
    # Build-in function to capitalize character
    capitalizedSentence = sentence.upper()
    # Send back modified message to client
    connectionSocket.send(capitalizedSentence)
    # connection/client socket close
    connectionSocket.close()