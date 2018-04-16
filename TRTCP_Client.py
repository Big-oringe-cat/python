#!/root/bin/python3

from twisted.internet import protocol, reactor

host = 'localhost'
port = 9999

class TCP(protocol.Protocol):#TwistedClientProtocol,not tcp
    def sendData(self):
        data = input(">>>")
        if data:
            print("正在发送消息:" + data)
            self.transport.write(data.encode('utf-8'))
        else:
            self.transport.loseConnection()
    
    def connectionMade(self):
        self.sendData()
    
    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()

class TCF(protocol.ClientFactory):
    protocol = TCP
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()

reactor.connectTCP(host, port, TCF())
reactor.run()
