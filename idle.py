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
        
        self.idle_status = "You are in Idle State, exit the window to move states"
        #Set up GPIO Interrupts
        #GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(24, GPIO.RISING, callback=self.call_24, bouncetime=300)
        GPIO.add_event_detect(16, GPIO.RISING, callback=self.call_16, bouncetime=300)
        
#         #create response variable to track when user wants to exit Idle state
#         #create messagebox show info pop up window for user input
#         self.response = 'continue'
#         self.response = messagebox.showinfo("Idle State", "Hit OK to Exit Idle State")
        #call top window
        self.idle_top = Toplevel()
        self.idle_top.title("Idle")
        
        #create prompt labels
        self.title_idle = Label(self.idle_top, text = self.idle_status,font=("Arial", 24), width=50, borderwidth=5)
        
        #place prompt labels
        self.title_idle.grid(row=0, column = 0, columnspan = 2)
        
        return
        
     
    #function called when button 24 is hit
    def call_24(self, channel):
        self.idle_status = "ACTIVE STATE ENGAGED. EXIT THE WINDOW AFTER INCIDENT FOR RESET"
        self.title_idle.config(text=self.idle_status)
        print("I am in 24")
        call_floor_24 = Floor(24)
        call_floor_24.send_message(self.location_info, "24")
        call_floor_24.client.disconnect()
        return
        
    #function called when button 16 is hit
    def call_16(self, channel):
        self.idle_status = "ACTIVE STATE ENGAGED. EXIT THE WINDOW AFTER INCIDENT FOR RESET"
        self.title_idle.config(text=self.idle_status)
        print("I am in 16")
        call_floor_16 = Floor(16)
        call_floor_16.send_message(self.location_info, "16")
        call_floor_16.client.disconnect()
        return



