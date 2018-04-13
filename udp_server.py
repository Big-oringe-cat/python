#!/root/bin/python3

import socket
from time import ctime

host = '127.0.0.1'
port = 9999
bufsize = 1024
addr = (host, port)

us = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
us.bind(addr)

while True:
    print('等待消息...')
    data, addr = us.recvfrom(bufsize)
    msg = '[%s] %s' % (ctime(), data.decode('utf-8'))
    us.sendto(msg.encode('utf-8'), addr)
    print("收到并返回消息给 " + str(addr))
us.close()
