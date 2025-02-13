import random
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    insults = []
    def add_insult(insult):
        if(insults.__contains__(insult)):
            return 'Insult repeated'
        insults.append(insult)
        return insult
    
    def get_insults():
        print(insults)
        return insults
    
    def insult_me():
        insult = insults.__getitem__(random.randint(0, len(insults)))
        print(insult)
        return insult

    server.register_function(insult_me, "insult_me")
    server.register_function(get_insults, "get_insults")
    server.register_function(add_insult, "add_insult")
    # Run the server's main loop
    server.serve_forever()