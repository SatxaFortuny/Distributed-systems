import redis
import time

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

queue_name = "insult_queue"

# Send multiple messages
insult_list = ["insult1", "insult2", "insult3", "insult4", "insult5", "insult1", "insult2", "insult3", "insult2"]

for task in insult_list:
    client.rpush(queue_name, task)
    print(f"Produced: {task}")
    time.sleep(1)  # Simulating a delay in task production
