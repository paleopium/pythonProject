import serial
import time
import statistics

class ArduinoReader():

    def __init__(self):
        super().__init__()
        # Establish serial connection
        self.serial_obj = serial.Serial('COM7', 115200)  # Replace 'COM7' with the appropriate port for your system
        # Set the duration of data collection (in seconds)
        self.duration = 8

    #median 1 and 2



    def calculate_the_data(self):
        print("GO")
        # Create an empty list to store the sensor data
        sensor_data = []

        # Get the start time
        start_time = time.time()

        # Read sensor data for the specified duration
        while (time.time() - start_time) < self.duration:
            if self.serial_obj.in_waiting > 0:
                # Read data from Arduino
                data = self.serial_obj.readline().decode().rstrip()

                # Convert data to float (assuming the sensor data is in floating-point format)
                try:
                    data = float(data)
                except ValueError:
                    continue

                # Append data to the sensor_data list
                sensor_data.append(data)
            return statistics.median(sensor_data)


