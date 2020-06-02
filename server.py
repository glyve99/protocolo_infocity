import socket
import threading
import json
from config import consts
from message import messageMaker

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(consts['ADDR']())

def fakeAuthIP(ip):
    return ip in consts['PERMITED_IPS']

def fakeAuthDevice(_id):
    return _id in consts['PERMITED_DEVICES']

def sendToClient(msg, conn):
    message = msg.encode(consts['FORMAT'])
    msg_length = len(message)
    send_length = str(msg_length).encode(consts['FORMAT'])
    send_length += b' ' * (consts['HEADER'] - len(send_length))
    conn.send(send_length)
    conn.send(message)

def handle_client(conn, addr):
    connected = True
    while connected:
        msg_length = conn.recv(consts['HEADER']).decode(consts['FORMAT']) #conn.receive
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(consts['FORMAT'])
            print(f'[{addr}] {msg}')
            msg = json.loads(msg)
            code = msg['code']

            if code == 101:
                if fakeAuthDevice(int(msg['param'][0])):
                    sendToClient(json.dumps(messageMaker(201)), conn)
                else:
                    sendToClient(json.dumps(messageMaker(204)), conn)
            if code == 103:
                if len(consts['PERMITED_DEVICES']) <= 5:
                    sendToClient(json.dumps(messageMaker(206)), conn)
                    sendToClient(json.dumps(messageMaker(207)), conn)
                else:
                    sendToClient(json.dumps(messageMaker(209)), conn)
            if code == 104:
                try:
                    consts['PERMITED_DEVICES'].append(msg['param'][0])
                except:
                    sendToClient(json.dumps(messageMaker(210)), conn)
            if code == 105:
                if msg['param'][0] == consts['SECURITY_KEY']:
                    sendToClient(json.dumps(messageMaker(208)), conn)
                else:
                    sendToClient(json.dumps(messageMaker(211)), conn)
            if code == 102:
                try:
                    connected = False
                    sendToClient(json.dumps(messageMaker(202)), conn)
                except:
                    sendToClient(json.dumps(messageMaker(205)), conn)

            print(f'[{addr}] {msg}')
    
    conn.close()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')


print('[STARTING] server is starting...')
start()
