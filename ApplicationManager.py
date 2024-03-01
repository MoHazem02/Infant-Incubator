from serial import *
from PyQt5 import QtCore
import soundfile as sf
import sounddevice as sd

class ApplicationManager:
    def __init__(self,UI):
        self.ui = UI
        self.serial_port = Serial('COM4', 9600)
        self.boundry_temp = 27
        self.start()
        self.data,self.sample_rate = sf.read("alert_sound.wav")
        
    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.read_data)
        self.timer.start(500) 

    def read_data(self):
        arduino_data = self.serial_port.readline().decode('utf-8').strip()

        if arduino_data:
            temprature, str2 = arduino_data.split(';')
            humidity, heart_rate = str2.split(',')
            self.ui.humidity_LCD.display(humidity)
            self.ui.BPM_LCD.display(heart_rate)
            self.ui.temp_LCD_2.display(temprature)
            self.ui.temp_LCD.display(self.boundry_temp)

            if (int(temprature) < self.boundry_temp):
                self.ui.Status_Frame.setStyleSheet("image: url(:/newPrefix/warning.png);")
                sd.play(self.data, self.sample_rate)
            else:
                self.ui.Status_Frame.setStyleSheet("image: url(:/newPrefix/checked.png);")
                sd.stop()
                
    
    def increment_boundry_temp(self):
        self.boundry_temp += 1

    def decrement_boundry_temp(self):
        self.boundry_temp -= 1