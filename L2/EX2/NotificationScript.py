# saved as greeting-client.py
import Pyro4

greeting_maker = Pyro4.Proxy("PYRONAME:example.observable") # use name server␣

print(greeting_maker.notifyAllObservers("Hello, Observers!"))
