from socket import *
import threading
import uuid

host = '127.0.0.1'
port = 15000

self_ID = uuid.uuid4()
foreign_ID = None

# as server
# accept connection
# receive UUID from others
# determine if forward or not
# maintain connection

def server_set_up():
    sc = socket(AF_INET, SOCK_STREAM)
    sc.bind((host, port))
    sc.listen(1)
    print(f'server listen at {host}:{port}')
    client, addr = sc.accept()
    print(f"New connection from {addr}")
    threading.Thread(target= server_process(), args= client)

def server_process(client):
    global foreign_ID

    foreign_ID = client

# as client
# connect to server
# send UUID (self)
# forward UUID (others/leader)


    '''
    if self.state == 1:
        if msg.flag == 1:
            self.log(f"Received: uuid={msg.uuid}, flag={msg.flag}, {comparison}, {self.state}, leader={self.leader_id}")
        else:
            self.log(f"Received: uuid={msg.uuid}, flag={msg.flag}, {comparison}, {self.state}, ignored")
        return

    self.log(f"Received: uuid={msg.uuid}, flag={msg.flag}, {comparison}, {self.state}")
    
    if msg.flag == 1:
        self.leader_id = msg.uuid
        self.state = 1
        self.send_message(msg.uuid, 1)
        self.log(f"Leader is decided to {msg.uuid}.")
    elif msg.uuid == str(self.my_uuid):
        self.leader_id = msg.uuid
        self.state = 1
        self.send_message(msg.uuid, 1)
        self.log(f"Leader is decided to {msg.uuid}.")
    elif msg.uuid > str(self.my_uuid):
        self.send_message(msg.uuid, 0)
    else:
        self.log("Message ignored.")'''