#!/root/bin/python3

from twisted.internet import protocol, reactor
from time import ctime

port = 9999

class TSP(protocol.Protocol):
    def connectionMade(self):
        client = self.client = self.transport.getPeer().host
        print("链接来自：", client)
    def dataReceived(self, data):
        msg = "[%s] %s" % (ctime(), data.decode("utf-8"))
        self.transport.write(msg.encode("utf-8"))

factory = protocol.Factory()
factory.protocol = TSP
print("等待链接")
reactor.listenTCP(port, factory)
reactor.run()
