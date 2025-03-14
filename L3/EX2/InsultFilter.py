import redis

# Connect to Redis
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

queue_name = "insult_queue"
insults_register = ["insult1", "insult2", "insult3", "insult5"]
client.delete("result_list")

print("Consumer is waiting for insults...")

while True:
    task = client.blpop(queue_name, timeout=0)  # Blocks indefinitely until a task is available
    if task:
        message = task[1]
        for insult in insults_register:
            message = message.replace(insult, "CENSORED")
        print(f"Consumed: {task[1]}")
        print(f"Filtered message: {message}")
        client.lpush("result_list", message)
        message_list = client.lrange("result_list", 0, -1)
        print(f"updated list: {message_list}")
