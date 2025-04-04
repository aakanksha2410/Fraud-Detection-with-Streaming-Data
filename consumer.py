from kafka import KafkaConsumer
import json
import joblib
import pandas as pd
import snowflake.connector

# Load model
model = joblib.load("model/fraud_model.pkl")

# Snowflake connection (replace with your credentials)
conn = snowflake.connector.connect(
    user="your_user",
    password="your_password",
    account="your_account",
    warehouse="your_warehouse",
    database="your_db",
    schema="your_schema"
)

# Initialize consumer
consumer = KafkaConsumer("transactions",
                         bootstrap_servers="localhost:9092",
                         value_deserializer=lambda x: json.loads(x.decode("utf-8")))

# Process stream
print("Starting consumer...")
for message in consumer:
    transaction = message.value
    features = pd.DataFrame([transaction]).drop("Class", axis=1)
    prediction = model.predict(features)[0]
    
    # Log to Snowflake
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO fraud_logs (time, amount, is_fraud) VALUES (%s, %s, %s)",
        (transaction["Time"], transaction["Amount"], bool(prediction))
    )
    conn.commit()
    
    print(f"Time: {transaction['Time']}, Amount: {transaction['Amount']}, Fraud: {bool(prediction)}")
conn.close()