import paho.mqtt.client as mqtt
import time
import random  # Used to simulate sensor data

# MQTT broker configuration
BROKER_ADDRESS = "broker.hivemq.com"  # Example public broker
TOPIC = "hotel/branch1/room1/temperature"

def read_temperature_sensor():
    # Simulate sensor reading
    temperature = round(random.uniform(18, 30), 2)
    return temperature

def publish_temperature(client):
    while True:
        temperature = read_temperature_sensor()
        payload = f"{temperature}"
        client.publish(TOPIC, payload)
        print(f"Publishing temperature: {temperature}°C to topic {TOPIC}")
        time.sleep(60)  # 60 seconds delay

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    publish_temperature(client)

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect

    client.connect(BROKER_ADDRESS, 1883, 60)
    client.loop_forever()