# saved as greeting-server.py
import Pyro4

@Pyro4.expose
class ObServer(object):
    receivedMessages = []

    def notify(self, message):
        self.receivedMessages.append(message)
        print(self.receivedMessages)
        return "message received"

daemon = Pyro4.Daemon() # make a Pyro daemon
ns = Pyro4.locateNS() # find the name server
serveruri = ns.lookup("example.observable")
server = Pyro4.Proxy(serveruri)
uri = daemon.register(ObServer) # register the greeting maker as a Pyro object
print(server.registerObserver(str(uri)))
print("Ready.")
daemon.requestLoop() # start the event loop of the server to wait for