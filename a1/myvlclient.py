import socket

serverName = 'localhost' #ip address

serverPort = 12000
chunk_length = 64 # defines the length of each transaction

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((serverName, serverPort))  # TCP requires a connection

message = input('Input lowercase sentence:')

try:
    length_of_message = int(message[0:2])
except ValueError:
    print('The first 2 characters should specify the length of the string')
    print('aborting...')
    exit(1)

# Slice the message into chunks of the length defined
message_list = \
    [message[i:i+chunk_length] for i in range(2, len(message), chunk_length)]

#debug
print(message_list)

#send the length of message to server
clientSocket.sendto(str(length_of_message).encode(),
                    (serverName, serverPort))
status, serverAddress = clientSocket.recvfrom(64)
print(f'status: {"OK" if status else "Error loading length of message"}')

for i in range(len(message_list)):
    try:
        clientSocket.sendto(message_list[i].encode(),
                            (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(64)
        print(f'chunk# {i}, msg: {modifiedMessage.decode()}')
    except socket.error as err:
        print(f'Error at chunk# {i}:, msg: {str(err)}')

# send complete signal
#close the socket once everything is transformed
clientSocket.close()