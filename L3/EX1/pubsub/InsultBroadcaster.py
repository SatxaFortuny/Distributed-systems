import redis
import time

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

channel_name = "insults_channel"

# Publish multiple messages
messages = ["insult1", "insult2", "insult3", "insult4", "insult5", "insult1", "insult2", "insult3", "insult2"]

for message in messages:
    client.publish(channel_name, message)
    print(f"Published: {message}")
    time.sleep(2)  # Simulating delay between messages
