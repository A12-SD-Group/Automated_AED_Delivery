import RPi.GPIO as GPIO
from tkinter import *
from PIL import ImageTk,Image
#needed to use messagebox
from tkinter import messagebox
from floor import *
import csv
import time

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
        self.call_floor = None
        #Set up GPIO Interrupts [18, 24, 12, 20] = floor [1, 2, 3, 4]
        #GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(24, GPIO.RISING, callback=self.call_24, bouncetime=300)
        #GPIO.add_event_detect(16, GPIO.RISING, callback=self.call_16, bouncetime=300)
        
#         #create response variable to track when user wants to exit Idle state
#         #create messagebox show info pop up window for user input
#         self.response = 'continue'
#         self.response = messagebox.showinfo("Idle State", "Hit OK to Exit Idle State")
        #call top window
        self.idle_top = Toplevel()
        self.idle_top.title("Idle")
        
        #create prompt labels
        self.title_idle = Label(self.idle_top, text = self.idle_status,font=("Arial", 14), width=75, borderwidth=5)
        
        #place prompt labels
        self.title_idle.grid(row=0, column = 0, columnspan = 2)
        
        self.idle_top.update()
        
#         no_call = True
#         while no_call:
#         #Set up GPIO Interrupts [18, 24, 12, 20] = floor [1, 2, 3, 4]
#             input1 = input()
#             if input1 == "one":
#                 self.call_1()
#                 no_call = False
#             elif input1 == "two":
#                 self.call_2()
#                 no_call = False
#             elif input1 == "three":
#                 self.call_3()
#                 no_call = False
#             elif input1 == "four":
#                 self.call_4()
#                 no_call = False
        
        no_call = True
        while no_call:
        #Set up GPIO Interrupts [18, 24, 12, 20] = floor [1, 2, 3, 4]
            
            if GPIO.input(18) == GPIO.HIGH:
                self.call_1()
                no_call = False
            elif GPIO.input(24) == GPIO.HIGH:
                self.call_2()
                no_call = False
            elif GPIO.input(12) == GPIO.HIGH:
                self.call_3()
                no_call = False
            elif GPIO.input(20) == GPIO.HIGH:
                self.call_4()
                no_call = False
            
        return
        
    #Set up GPIO Interrupts [18, 24, 12, 20] = floor [1, 2, 3, 4]
    #function called when GPIO18 button (floor 1) is hit
    def call_1(self):
        self.idle_status = "ACTIVE STATE ENGAGED. EXIT THE WINDOW AFTER INCIDENT FOR RESET"
        self.title_idle.config(text=self.idle_status)
        self.idle_top.update()
        self.call_floor = 1
        print("I am in 1")
        call_floor_1 = Floor(1)
        call_floor_1.send_message(self.location_info, "1")
        call_floor_1.client.disconnect()
        return
    
    #function called when GPIO24 button (floor 2) is hit
    def call_2(self):
        self.idle_status = "ACTIVE STATE ENGAGED. EXIT THE WINDOW AFTER INCIDENT FOR RESET"
        self.title_idle.config(text=self.idle_status)
        self.idle_top.update()
        self.call_floor = 2
        print("I am in 2")
        call_floor_2 = Floor(2)
        call_floor_2.send_message(self.location_info, "2")
        call_floor_2.client.disconnect()
        return
    
    #function called when GPIO12 button (floor 3) is hit
    def call_3(self):
        self.idle_status = "ACTIVE STATE ENGAGED. EXIT THE WINDOW AFTER INCIDENT FOR RESET"
        self.title_idle.config(text=self.idle_status)
        self.idle_top.update()
        print("I am in 3")
        self.call_floor = 3
        call_floor_3 = Floor(3)
        call_floor_3.send_message(self.location_info, "3")
        call_floor_3.client.disconnect()
        return
    
    #function called when GPIO20 button (floor 4) is hit
    def call_4(self):
        self.idle_status = "ACTIVE STATE ENGAGED. EXIT THE WINDOW AFTER INCIDENT FOR RESET"
        self.title_idle.config(text=self.idle_status)
        self.idle_top.update()
        self.call_floor = 4
        print("I am in 4")
        call_floor_4 = Floor(4)
        call_floor_4.send_message(self.location_info, "4")
        call_floor_4.client.disconnect()
        return
        
    



