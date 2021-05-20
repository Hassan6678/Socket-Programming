import socket
serverName = 'localhost'
serverPort = 12000
'''
Create a socket
socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
'''
clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Take user Input
message = input("Input lowercase sentence:")

''' 
Method sendto() attaches the destination address (serverName, serverPort)
to the message and sends the resulting packet into the process’s socket, clientSocket
'''
clientSocket.sendto(message.encode(),(serverName, serverPort))

# Received message from server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# Show result on Console
print (modifiedMessage.decode())

# Socket closes
clientSocket.close()