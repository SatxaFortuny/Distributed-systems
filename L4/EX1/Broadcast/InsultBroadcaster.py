import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a fanout exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')
insult_list = ["insult1", "insult2", "insult3", "insult4", "insult5", "insult1", "insult2", "insult3", "insult2"]
# Publish a message
for i in range(len(insult_list)):
    message = insult_list[i]
    channel.basic_publish(exchange='logs', routing_key='', body=message)
    print(f" [x] Sent '{message}'")

print(f"Finished")

# Close connection
connection.close()
