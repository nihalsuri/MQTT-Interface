import json
import paho.mqtt.client as mqtt


class MQTTSubscriber:
    def __init__(self, broker="test.mosquitto.org", port=1883, topic="m/plc/sensor", on_message_callback=None):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.on_message_callback = on_message_callback
        self.client = mqtt.Client()

        # Attach the message callback
        self.client.on_message = self.on_message

        # Connect to the broker and subscribe to the topic
        self.client.connect(self.broker, self.port)
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, message):
        """Handle incoming messages and trigger the callback."""
        try:
            payload = message.payload.decode()
            message_data = json.loads(payload)  # Parse JSON message
            if self.on_message_callback:
                self.on_message_callback(message_data)
        except json.JSONDecodeError:
            print("Invalid JSON received")

    def start(self):
        """Start the loop to listen for incoming messages."""
        self.client.loop_start()

    def stop(self):
        """Stop the loop when done."""
        self.client.loop_stop()

