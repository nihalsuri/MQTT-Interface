import json
import paho.mqtt.client as mqtt


class MQTTPublisher:
    def __init__(self, broker="test.mosquitto.org", port=1883, topic="m/plc/sensor"):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()

        # Connect to the broker
        self.client.connect(self.broker, self.port)

    def publish_message(self, message):
        """Publish the given message (as a JSON string) to the MQTT broker."""
        message_json = json.dumps(message)
        self.client.publish(self.topic, message_json)
        print("Message Published:", message_json)
