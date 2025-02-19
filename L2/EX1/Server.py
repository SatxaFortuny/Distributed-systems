# saved as greeting-server.py
import Pyro4

@Pyro4.expose
class EchoServer(object):
    def echo(self):
        print("Hola")
        return "Hola"

daemon = Pyro4.Daemon() # make a Pyro daemon
ns = Pyro4.locateNS() # find the name server
uri = daemon.register(EchoServer) # register the greeting maker as a Pyro object
ns.register("echo.server", uri) # register the object with a name in the name␣

print("Ready.")
daemon.requestLoop() # start the event loop of the server to wait for