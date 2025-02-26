# saved as greeting-server.py
import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class ObservableServer:
    
    def __init__(self):
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)
        print("observer registered")
        return "observer registered"

    def unregisterObserver(self, observer):
        self.observers.remove(Pyro4.Proxy("PYRONAME:"+observer))
        print("server unregistered")
        return "server unregistered"

    def notifyAllObservers(self, name):
        for observer in self.observers:
            obsvr = Pyro4.Proxy(observer)
            print(f"Observer: {observer} | {obsvr.notify(name)}")
        return "All observers notified"

daemon = Pyro4.Daemon() # make a Pyro daemon
ns = Pyro4.locateNS() # find the name server
uri = daemon.register(ObservableServer) # register the greeting maker as a Pyro object
ns.register("example.observable", uri) # register the object with a name in the name␣
print("Ready.")
daemon.requestLoop()
# start the event loop of the server to wait for