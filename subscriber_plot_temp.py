import paho.mqtt.client as mqtt
import json
import matplotlib.pyplot as plt
import csv
import time

BROKER = "test.mosquitto.org"
TOPIC = "test/topic/json"
CSV_FILE = "sensor_data.csv"

heart_rates = []
spo2_values = []
temperatures = []

plt.ion()
fig, ax = plt.subplots(3, 1, figsize=(8, 8))

def update_plot():
    ax[0].cla()
    ax[1].cla()
    ax[2].cla()
    ax[0].plot(heart_rates, marker="o", color="red")
    ax[0].set_title("Heart Rate")
    ax[0].set_ylabel("BPM")
    ax[1].plot(spo2_values, marker="o", color="blue")
    ax[1].set_title("SpO2")
    ax[1].set_ylabel("%")
    ax[2].plot(temperatures, marker="o", color="green")
    ax[2].set_title("Temperature")
    ax[2].set_ylabel("°C")
    plt.tight_layout()
    plt.pause(0.01)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        heart_rate = data["heart_rate"]
        spo2 = data["spo2"]
        temperature = data["temperature"]

        heart_rates.append(heart_rate)
        spo2_values.append(spo2)
        temperatures.append(temperature)

        with open(CSV_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([time.time(), heart_rate, spo2, temperature])

        update_plot()
    except json.JSONDecodeError:
        print("Received non JSON message:", msg.payload.decode())

client = mqtt.Client("Subscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_forever()

