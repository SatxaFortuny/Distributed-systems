import pika
import redis
# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
queue_name = "insult_queue"
client.delete("insults_register")

# Declare a queue (ensure it exists)
channel.queue_declare(queue='insult')

# Define the callback function
def callback(ch, method, properties, body):
    insult = body.decode()
    print(f" [x] Received {insult}")
    insults_register = client.lrange("insults_register", 0, -1)
    if insult not in insults_register:
        client.lpush("insults_register", insult)
        print("insult added to list")
    insults_register = client.lrange("insults_register", 0, -1)
    print(f"updated list: {insults_register}")

# Consume messages
channel.basic_consume(queue='insult', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()