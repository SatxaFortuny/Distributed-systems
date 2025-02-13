import random
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.client import ServerProxy


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    subjects = []
    insults = []
    def add_insult(insult):
        if insult in insults:
            return 'Insult repeated'
        insults.append(insult)
        notifyAllObservers(insult)
        return insult
    
    def get_insults():
        print(insults)
        return insults
    
    def insult_me():
        insult = insults.__getitem__(random.randint(0, len(insults)-1))
        print(insult)
        return insult

    def register(ip):
        sub = ServerProxy(ip)
        subjects.append(sub)
        return ip

    def notifyAllObservers(insult):
        for sub in subjects:
            sub.notify(insult)

    def notify(insult):
        print('8000 '+insult)
        return insult

    server.register_function(insult_me, "insult_me")
    server.register_function(get_insults, "get_insults")
    server.register_function(add_insult, "add_insult")
    server.register_function(notify, "notify")
    server.register_function(register, "register")
    # Run the server's main loop
    server.serve_forever()