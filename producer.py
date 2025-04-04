from kafka import KafkaProducer
import json
import pandas as pd
import time

# Initialize producer
producer = KafkaProducer(bootstrap_servers="localhost:9092",
                         value_serializer=lambda v: json.dumps(v).encode("utf-8"))

# Load data
data = pd.read_csv("data/creditcard.csv")

# Send transactions to Kafka
print("Starting producer...")
for i, (_, row) in enumerate(data.iterrows()):
    transaction = row.to_dict()
    producer.send("transactions", value=transaction)
    if i % 1000 == 0:
        print(f"Sent {i} transactions")
    time.sleep(0.1)  # Simulate real-time
producer.flush()
print("Producer finished.")