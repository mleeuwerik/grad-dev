from twisted.internet import reactor, protocol

ip = "localhost"
port = 8000


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello, world!".encode())

    def dataReceived(self, data):
        print("Server said: ", data)


class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost!")
        reactor.stop()


reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()