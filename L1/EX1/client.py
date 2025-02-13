import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.add_insult('Hola'))


print(s.system.listMethods())