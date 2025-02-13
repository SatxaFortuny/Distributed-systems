import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')

print(s.register('http://localhost:8001'))
print(s.add_insult('Hola'))
print(s.register('http://localhost:8002'))
print(s.add_insult('Adeu'))
print(s.register('http://localhost:8003'))
print(s.register('http://localhost:8004'))
print(s.add_insult('BonDia'))
print(s.get_insults())
print(s.insult_me())

print(s.system.listMethods())