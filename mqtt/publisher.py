import paho.mqtt.client as mqtt

# Define the broker details
broker = "test.mosquitto.org"
port = 1883
topic = "m/plc/sensor"

# Callback when the message has been published
def on_publish(client, userdata, result):
    print("Message Published")

# Create an MQTT client instance
client = mqtt.Client()

# Attach the on_publish callback function
client.on_publish = on_publish

# Connect to the broker
client.connect(broker, port)

# Publish a message
message = "Hello from MQTT publisher!"
client.publish(topic, message)

# Disconnect from the broker
client.disconnect()
