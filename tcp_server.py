#!/root/bin/python3

import socket
import sys
import subprocess
import threading

#创建socket对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

#获取本地主机名
host = str(socket.gethostname())

port = 9999

#绑定端口号
serversocket.bind((host,port))

#设置最大连接数，超过后排队
serversocket.listen(2)

def tcplink(socket,address):
    while 1:
            data=socket.recv(1024)
            c_status, c_result = subprocess.getstatusoutput(data.decode('utf-8'))
            try:
                if (c_status == 0):
                    if (c_result == 'quit'):
                        socket.close()
                        break
                    else:
                        msg = '结果为:' + c_result
                        socket.sendall(msg.encode('utf-8'))
                else:
                    msg = '错误为:' + c_result
                    socket.sendall(msg.encode('utf-8'))
            except BrokenPipeError:
                print("对方可能使用了快捷键退出了客户端，连接中断")
                socket.close()
                break


while True:
    try:
        #建立客户端连接
        clientsocket,addr = serversocket.accept()
        print("链接地址：%s" % str(addr))
        t=threading.Thread(target=tcplink, args=(clientsocket,addr))
        t.start()
    except KeyboardInterrupt:
        print('\r\n' + "服务端主动退出")
        serversocket.close()
        break
serversocket.close()
