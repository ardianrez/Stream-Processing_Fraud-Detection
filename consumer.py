import json
from kafka import KafkaConsumer

if __name__ == "__main__":
    consumer = KafkaConsumer("digitalskola-p6", bootstrap_servers='localhost')
    print("starting the consumer")
    for msg in consumer:
        print(f"Records = {json.loads(msg.value)}")