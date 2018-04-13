#!/root/bin/python3

import socket

host = '127.0.0.1'
port = 9999
bufsize = 1024
addr = (host, port)

uc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("请输入")
    if not data:
        break
    uc.sendto(data.encode("utf-8"), addr)
    data, addr = uc.recvfrom(bufsize)
    if not data:
        break
    print(data.decode("utf-8"))
us.close()
