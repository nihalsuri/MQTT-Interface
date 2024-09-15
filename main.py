import sys
import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMainWindow


class MQTTInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

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

    def on_publish_click(self):
        """Handle button click and display formatted JSON."""
        message = {
            "Time": "04/01/2023 00:00:00",
            "Temperature": 18,
            "Humidity": 10,
            "Sound_Level": 20,
            "Light_Level": 200
        }

        # Convert the dictionary to a formatted JSON string
        formatted_json = json.dumps(message, indent=4)

        # Display published MQTT message in the text box
        self.display_message(formatted_json)

    def display_message(self, message):
        """Display the given message in the text box."""
        self.text_box.setText(message)


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
