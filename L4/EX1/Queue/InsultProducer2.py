from time import sleep
import pika

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='insult')

# Publish a message
while True:
    channel.basic_publish(exchange='', routing_key='insult', body='insult2')
    print(" [x] Sent 'insult2'")
    sleep(5)

# Close connection
connection.close()
