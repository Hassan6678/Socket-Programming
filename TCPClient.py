from socket import *
serverName = 'localhost'
serverPort = 12000

'''
Create a socket
socket.AF_INET - address family, IPv4, some otehr possible are AF_INET6, AF_BLUETOOTH, AF_UNIX
socket.SOCK_STREAM - TCP, conection-based, socket.SOCK_DGRAM - UDP, connectionless, datagrams, socket.SOCK_RAW - raw IP packets
'''
clientSocket = socket(family=AF_INET, type=SOCK_STREAM)

# Connect to a given ip and port
clientSocket.connect((serverName,serverPort))

sentence = input('Input lowercase sentence:')

# send encoded message to server
clientSocket.send(sentence.encode())

# recieved modified message from
modifiedSentence = clientSocket.recv(1024)

# show message on console
print('From Server:', modifiedSentence.decode())

# connection close
clientSocket.close()