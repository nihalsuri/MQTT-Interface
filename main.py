import csv
import json
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMainWindow

from mqtt.publisher import MQTTPublisher
from mqtt.subscriber import MQTTSubscriber


class MQTTInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        # Initialize publisher
        self.publisher = MQTTPublisher()

        # Initialize subscriber
        self.subscriber = MQTTSubscriber(on_message_callback=self.display_message)
        self.subscriber.start()  # Start the subscriber loop

        self.csv_data = self.load_csv_data("Simulated_sensor_data.csv")
        self.current_record = 0

    def init_ui(self):
        """Initialize the UI layout and widgets."""
        # Create a vertical layout as requested in the task
        layout = QVBoxLayout()

        # Create a QTextEdit (all received messages would be displayed here)
        self.text_box = QTextEdit(self)
        self.text_box.setReadOnly(True)  # Make the box read-only

        # Create a QPushButton (this button publishes data on the broker each time pressed)
        self.button = QPushButton('Send', self)

        # Add the output message box and the button to the layout
        layout.addWidget(self.text_box)
        layout.addWidget(self.button)

        # Set the layout for the QWidget
        self.setLayout(layout)

        # Connect the button click event to the function
        self.button.clicked.connect(self.on_publish_click)

        # Set the window properties
        self.setWindowTitle('MQTT Interface')
        self.setGeometry(100, 100, 800, 500)
        self.show()

    def load_csv_data(self, file_path):
        """Load data from the CSV file."""
        csv_data = []
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    csv_data.append(row)  # Append each row as a dictionary
            return csv_data
        except FileNotFoundError:
            self.text_box.append("Error: CSV file not found!")
            return []

    def on_publish_click(self):
        """Handle button click and publish the next CSV record."""
        if self.current_record < len(self.csv_data):
            message = self.csv_data[self.current_record]

            # Publish the JSON message
            self.publisher.publish_message(message)

            # Move to the next record
            self.current_record += 1
        else:
            self.text_box.append("All records have been published.")

    def display_message(self, message):
        """Display the given message in the text box."""
        formatted_message = json.dumps(message, indent=4)
        self.text_box.append(formatted_message)
        # So that text box scrolls to the latest message
        self.text_box.ensureCursorVisible() 


class MQTTInterfaceDesigner(QMainWindow):
    """Initialize the UI layout from QT Designer."""

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/standard_interface.ui", self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # To consume UI from QTDesigner, change class name to MQTTInterfaceDesigner
    ex = MQTTInterface()
    sys.exit(app.exec_())

