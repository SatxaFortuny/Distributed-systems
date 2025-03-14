import redis

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

queue_name = "insult_queue"
print("Consumer is waiting for insults...")

while True:
    task = client.blpop(queue_name, timeout=0)  # Blocks indefinitely until a task is available
    if task:
        insult = task[1]
        insults_register = client.lrange("insults_register", 0, -1)
        if insult not in insults_register:
            client.lpush("insults_register", insult)
            print("insuld added to list")
        print(f"Consumed: {task[1]}")
        insults_register = client.lrange("insults_register", 0, -1)
        print(f"updated list: {insults_register}")
