from socket import *

serverName = 'localhost' #ip address

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print("server is listening")
while True:

    cnSocket, addr = serverSocket.accept()
    sentence = cnSocket.recv(64).decode()


    capSentence = sentence.upper()

    cnSocket.send(capSentence.encode())

    cnSocket.close()