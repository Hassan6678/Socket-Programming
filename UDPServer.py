from socket import *

serverPort = 12000
'''
Create a socket
socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
'''
serverSocket = socket(family=AF_INET, type=SOCK_DGRAM)
# Bind, so server informs operating system that it's going to use given IP and port
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    # Build-in fucntion use to capitalize the character
    modifiedMessage = message.upper()
    # Server back send Modified Message to client address
    serverSocket.sendto(modifiedMessage, clientAddress)