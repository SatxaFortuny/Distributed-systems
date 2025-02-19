# saved as greeting-client.py
import Pyro4

greeting_maker = Pyro4.Proxy("PYRONAME:echo.server") # use name server␣

print(greeting_maker.echo())
