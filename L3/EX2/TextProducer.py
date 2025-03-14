import redis
import time

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

queue_name = "insult_queue"

# Send multiple messages
insult_list = ["hello", "good", "morning", "how", "are", "you"]

for task in insult_list:
    client.rpush(queue_name, task)
    print(f"Produced: {task}")
    time.sleep(5)  # Simulating a delay in task production
