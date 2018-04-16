#!/root/bin/python3

from socket import *
host = 'localhost'
port = 9999
bufsize =1024
addr = (host, port)

while True:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(addr)
    data = input(">>>")
    if not data:
        break
    data = data + '\r\n'
    s.send(data.encode('utf-8'))
    data = s.recv(bufsize)
    if not data:
        break
    print(data.decode('utf-8').strip())
    s.close()
