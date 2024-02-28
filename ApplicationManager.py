from serial import *
from PyQt5 import QtCore

class ApplicationManager:
    def __init__(self,UI):
        self.ui = UI
        self.serial_port = Serial('COM4', 9600)
        self.start()
        
    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(500) 

    def read_data(self):
        arduino_data = self.serial_port.readline().decode('utf-8').strip()
        if arduino_data:
            temprature_value, str2 = arduino_data.split(',')
            humidity, heart_rate = str2.split(';')
            
            self.ui.humidity_LCD.display(humidity)
            self.ui.BPM_LCD.display(heart_rate)
            self.ui.temp_LCD.display(heart_rate)

                
        

