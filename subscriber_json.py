import paho.mqtt.client as mqtt
import json

broker = "test.mosquitto.org"
port = 1883
topic = "test/topic"

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        heart_rate = data.get("heart_rate")
        spo2 = data.get("spo2")
        print(f"Received - Heart Rate: {heart_rate} bpm, SpO2: {spo2}%")
    except json.JSONDecodeError:
        print(f"Received non-JSON message: {msg.payload.decode()}")

client = mqtt.Client("SubscriberJSON")
client.on_message = on_message
client.connect(broker, port)
client.subscribe(topic)
print(f"Subscribed to topic: {topic}")
client.loop_forever()

