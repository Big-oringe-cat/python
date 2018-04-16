#!/root/bin/python3

from socketserver import (TCPServer as TCP,
     StreamRequestHandler as SRH,
     ThreadingMixIn as TMI)
#from socketserver import (TCPServer as TCP,
#     StreamRequestHandler as SRH,
#     ForkingMixIn as FMI)
from time import ctime

host = ''
port = 9999
addr = (host, port)

class Server(TMI, TCP):
    pass

class MyRequestHandler(SRH):
    def handle(self):
        print("链接来自： " + str(self.client_address))
        msg = '[%s] %s' %(ctime(), self.rfile.readline().decode('utf-8'))
        self.wfile.write(msg.encode('utf-8'))

tcpServer = Server(addr, MyRequestHandler)
#tcpServer = TCP(addr, MyRequestHandler)
print('等待链接。。。')
tcpServer.serve_forever()
