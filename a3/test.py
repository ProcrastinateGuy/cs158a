import socket
import threading
from threading import Event


import time
import uuid
import json
import sys

class Message:
    def __init__(self, uuid_val: uuid.UUID, flag: int):
        self.uuid = str(uuid_val)  # UUIDs must be stringifies for JSON
        self.flag = flag

    def to_json(self):
        return json.dumps(self.__dict__) + "\n"

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str.strip())
        return Message(uuid.UUID(data['uuid']), data['flag'])

class LeaderNode:
    def __init__(self, config_path= sys.argv[1]):
        self.my_uuid = uuid.uuid4()
        self.leader_id = None
        self.state = 0  # 0: election ongoing, 1: leader decided
        self.load_config(config_path)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_ready = Event()
        self.log_file = open('log.txt', 'a')

    def load_config(self, path):
        with open(path, 'r') as f:
            lines = f.read().splitlines()
            self.server_ip, self.server_port = lines[0].split(',')
            self.client_ip, self.client_port = lines[1].split(',')
            self.server_port = int(self.server_port)
            self.client_port = int(self.client_port)

    def log(self, msg):
        print(msg)
        self.log_file.write(msg + '\n')
        self.log_file.flush()

    def start(self):
        threading.Thread(target=self.start_server).start()
        time.sleep(5)  # wait for server to start
        self.connect_to_client()
        self.send_message(self.my_uuid, 0)  # send initial message

    def start_server(self):
        self.server_socket.bind((self.server_ip, self.server_port))
        self.server_socket.listen(1)
        conn, _ = self.server_socket.accept()
        while True:
            msg = self.receive_message(conn)
            if msg:
                self.handle_message(msg)

    def connect_to_client(self):
        while True:
            try:
                self.client_socket.connect((self.client_ip, self.client_port))
                self.client_ready.set()  # mark client as ready
                break
            except:
                time.sleep(1)

    def receive_message(self, conn):
        buffer = ""
        while True:
            chunk = conn.recv(1024).decode()
            if not chunk:
                return None
            buffer += chunk
            if "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                return Message.from_json(line)

    def send_message(self, uuid_val, flag):
        msg = Message(uuid_val, flag)
        self.client_ready.wait()
        self.client_socket.send(msg.to_json().encode())
        self.log(f"Sent: uuid={msg.uuid}, flag={msg.flag}")

    def handle_message(self, msg):

        #special case: leader msg received
        if msg.flag == 1:
            if self.leader_id != msg.uuid: # if this is the first time we see the leader
                self.leader_id = msg.uuid
                self.log(f"Leader is decided to {msg.uuid}.")
            else: #if the same leader comes again -> stop the flow
                return

        comparison = "same"

        if msg.uuid == str(self.my_uuid):
            # I'm the leader
            self.send_message(self.my_uuid, 1)
            self.log(f"I'm the leader")
            self.log(f"sending my own uuid: {self.my_uuid}")

        elif msg.uuid > str(self.my_uuid):
            # forward that id
            comparison = "greater"
            self.send_message(msg.uuid, msg.flag)
            self.log(f"Received: uuid={msg.uuid}, flag={msg.flag}, {comparison}, {self.state}, forwarded")

        elif msg.uuid < str(self.my_uuid):
            # forward my own uuid
            comparison = "less"
            self.send_message(self.my_uuid, 0)
            self.log(f"Received: uuid={msg.uuid}, flag={msg.flag}, {comparison}, {self.state}, ignored")
            self.log(f"sending my own uuid: {self.my_uuid}")


if __name__ == '__main__':
    node = LeaderNode()
    node.start()
