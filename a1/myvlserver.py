from math import trunc
from socket import *

serverName = 'localhost' #ip address

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print("server is listening")



while True:
    #set up connection and print out the IP and port
    cnSocket, addr = serverSocket.accept()
    print(f'Connection established with {addr[0]} at port {addr[1]}')

    #extract the length of the message
    length = int(cnSocket.recv(64).decode())
    number_of_transaction = trunc((length / 64) if (length % 64 == 0) else ((length/64) + 1))
    print(f'Number of transactions: {number_of_transaction}')

    cnSocket.send(str(isinstance(length, int)).encode())
    print(f"client specified length: {length}")

    actual_length = 0
    for _ in range(number_of_transaction):
        sentence = cnSocket.recv(64).decode()
        capSentence = sentence.upper()
        actual_length += len(sentence)
        cnSocket.send(capSentence.encode())

    print(f'client message actual length: {actual_length}')

    cnSocket.close()