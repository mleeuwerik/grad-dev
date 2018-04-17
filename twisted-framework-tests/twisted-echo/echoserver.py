from twisted.internet import protocol, reactor

port = 8000


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(port, EchoFactory())
reactor.run()

