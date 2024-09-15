# MQTT Interface
 Python application that can send and receive data to/from an MQTT broker.

 ## Getting Started
 Clone the repository, activate the virtual environment and install all dependencies: 
 ``` 
 git clone https://github.com/nihalsuri/MQTT-Interface.git
 python3 -m venv venv
 call venv\Scripts\activate.bat
 pip install PyQt5
``` 
Make sure to also add your own "Simulated_sensor_data.csv" file to the root of the project so that there is something to publish on the broker, if the name of the file is something different please updated the ".gitignore" file as well to keep the sensor data private and not upload it to the remote
## Application Functionality 
The application acts as an interface to publish data on the broker on a specific topic and view what the subscription on the same topic provides as an end result. The application can be broken down into the following: 
### Main UI
The main UI used was created using PyQt5, as this was a very basic UI: 
![UI made with PyQt5](images/uiBasic.png)

 the method to use QtDesigner would be a bit "overkill" according to me, but still as its quite a user friendly application an approach was also conducted with the same and can be found under **"ui/standard_interface.ui"** 

## Design Decisions 


## Future Improvements


## Difficulties Faced


## Recommendations to the main task