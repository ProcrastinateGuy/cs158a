from socket import *

serverName = 'localhost' #ip address

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) # TCP

clientSocket.connect((serverName, serverPort))  # TCP requires a connection

message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),
                    (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(64)
print(modifiedMessage.decode())
clientSocket.close()