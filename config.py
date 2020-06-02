import socket

consts = {
    'HEADER' : 16,
    'PORT' : 5000,
    'SERVER' : socket.gethostbyname(socket.gethostname()),
    'ADDR' : lambda : (consts['SERVER'], consts['PORT']),
    'FORMAT' : 'utf-8',
    'DISCONNECT_MESSAGE' : '!DISCONNECT',
    'PERMITED_IPS' : ['127.0.0.1'],
    'PERMITED_DEVICES' : [99999],
    'SECURITY_KEY' : 'guilhermeluanaluskastk'
}