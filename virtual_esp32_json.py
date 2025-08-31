import paho.mqtt.client as mqtt
import time
import random
import json

broker = "test.mosquitto.org"
port = 1883
topic = "test/topic"

client = mqtt.Client("VirtualESP32")
client.connect(broker, port)
print("Connected to broker. Sending simulated sensor data...")

try:
    while True:
        heart_rate = random.randint(60, 100)
        spo2 = random.randint(95, 100)
        data = {
            "heart_rate": heart_rate,
            "spo2": spo2
            "temperature": temerature 
        }
        message = json.dumps(data)
        client.publish(topic, message)
        print(f"Published: {message}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Simulation stopped")


