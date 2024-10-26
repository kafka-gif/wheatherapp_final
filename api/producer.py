from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

def create_producer():
    return KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

def generate_weather_data():
    regions = ["New York", "London", "Tokyo", "Sydney", "Paris"]
    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "region": random.choice(regions),
        "temperature": round(random.uniform(15.0, 30.0), 1),
        "precipitation": round(random.uniform(0, 1.0), 2),
        "humidity": random.randint(50, 90),
        "timestamp": datetime.now().isoformat()
    }

def run_producer():
    producer = create_producer()
    
    while True:
        try:
            weather_data = generate_weather_data()
            producer.send('weather_updates', weather_data)
            print(f"Sent: {weather_data}")
            time.sleep(5)  # Send new data every 5 seconds
        except Exception as e:
            print(f"Error sending message: {e}")
            time.sleep(5)

if __name__ == "__main__":
    run_producer()