import abc
class AbstractServer(abc.ABC):
    def __init__(self, version=1):
        self.version = version

    def get_version(self):
        return self.version

    @abc.abstractmethod
    def connect(self):
        pass

class IServer(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    @abc.abstractmethod
    def request(self):
        pass

    @abc.abstractmethod
    def responce(self):
        pass

class ServerApache(AbstractServer):
    def connect(self):
        print('Connection from Apache')

class ServerIIS(AbstractServer):
    def connect(self):
        print('Connection from IIS')

class Client:
    def connect_to(self, server):
        if isinstance(server, AbstractServer):
            server.connect()


serverIIS = ServerIIS()
cl = Client()
cl.connect_to(serverIIS)