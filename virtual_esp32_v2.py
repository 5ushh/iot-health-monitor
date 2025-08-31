import paho.mqtt.client as mqtt
import time
import json
import random

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "test/topic/json"

client = mqtt.Client("VirtualESP32")
client.connect(BROKER, PORT, 60)
print("Connected to broker. Sending simulated sensor data...")

try:
    while True:
        heart_rate = random.randint(60, 100)
        spo2 = random.randint(95, 100)
        temperature = round(random.uniform(36.5, 37.5), 1)
        payload = {"heart_rate": heart_rate, "spo2": spo2, "temperature": temperature}

        client.publish(TOPIC, json.dumps(payload))
        print(f"Published: {json.dumps(payload)}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Simulation stopped")
    client.disconnect()

