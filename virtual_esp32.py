import paho.mqtt.client as mqtt
import time
import random

broker = "test.mosquitto.org"
port = 1883
topic = "test/topic"

client = mqtt.Client("VirtualESP32")
client.connect(broker, port)
print("Connected to broker. Sending simulated sensor data...")

try:
    while True:
        heart_rate = random.randint(60, 100)  # simulate heart rate
        message = f"Heart Rate: {heart_rate}"
        client.publish(topic, message)
        print(f"Published: {message}")
        time.sleep(2)  # wait 2 seconds before next message
except KeyboardInterrupt:
    print("Simulation stopped")

