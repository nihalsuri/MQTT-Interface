import paho.mqtt.client as mqtt

# Define the broker details
broker = "test.mosquitto.org"
port = 1883
topic = "m/plc/sensor"

# Callback when a message is received
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Create an MQTT client instance
client = mqtt.Client()

# Attach the on_message callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker, port)

# Subscribe to the topic
client.subscribe(topic)

# Start the loop to process received messages
client.loop_start()

# Keep the script running
input("Press Enter to exit...\n")

# Stop the loop and disconnect
client.loop_stop()
client.disconnect()
