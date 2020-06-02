import socket
import sys
import json
from config import consts
from message import messageMaker


code = int(sys.argv[1])
if len(sys.argv) > 2:
    _id = []
    for arg in sys.argv[2:]:
        _id.append(arg)
    msg_ = messageMaker(code, _id)
else:
    msg_ = messageMaker(code)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(consts['ADDR']())


def send(msg):
    message = msg.encode(consts['FORMAT'])
    msg_length = len(message)
    send_length = str(msg_length).encode(consts['FORMAT'])
    send_length += b' ' * (consts['HEADER'] - len(send_length))
    client.send(send_length)
    client.send(message)
    res_length = client.recv(consts['HEADER']).decode(consts['FORMAT'])
    if res_length:
        res_length = int(res_length)
        res = client.recv(res_length).decode(consts['FORMAT'])
        print(res)

print(json.dumps(msg_))
send(json.dumps(msg_))