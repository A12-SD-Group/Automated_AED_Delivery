import RPi.GPIO as GPIO
from tkinter import *
from PIL import ImageTk,Image
#needed to use messagebox
from tkinter import messagebox
from floor import *
import csv

class Idle:
    
    def __init__(self, file_path):
             
        # create message from file_path
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            rows = list(csv_reader)
        
        message = rows[1]
        self.location_info = ""
        for i in range(0, len(message)):
            self.location_info += message[i]
            self.location_info += " "
            
        #Set up GPIO Interrupts
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(25, GPIO.FALLING, callback=self.call_25, bouncetime=300)
        GPIO.add_event_detect(16, GPIO.FALLING, callback=self.call_16, bouncetime=300)
        
        #create response variable to track when user wants to exit Idle state
        #create messagebox show info pop up window for user input
        self.response = 'continue'
        self.response = messagebox.showinfo("Idle State", "Hit OK to Exit Idle State")
        return
        
     
    #function called when button 25 is hit
    def call_25(self, channel):
        if (self.response != 'ok'):
            call_floor_25 = Floor(25)
            call_floor_25.send_message(self.location_info)
            call_floor_25.client.disconnect()
            return
        else:
            return
        
    #function called when button 16 is hit
    def call_16(self, channel):
        if (self.response != 'ok'):
            call_floor_16 = Floor(16)
            call_floor_16.send_message(self.location_info)
            call_floor_16.client.disconnect()
            return
        else:
            return


