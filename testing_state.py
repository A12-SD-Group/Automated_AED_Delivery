import os
import datetime
import csv
from tkinter import *
from PIL import ImageTk,Image
#needed to use messagebox
from tkinter import messagebox
from Data_class import *
import paho.mqtt.client as mqtt 


class Testing:
    def __init__(self, calibration_status = "not complete"):
        ## MQTT Setup
        self.client = mqtt.Client("AED_rasp_pi")
        self.client.username_pw_set("tuf53905@temple.edu", password="GMPQTtw7")
        self.client.connect("maqiatto.com", 1883, 60 )
        
        #variables
        self.calibration_complete = calibration_status
        
        ##GUI attributes
        self.test_top = Toplevel()
        self.test_top.title("Testing")
        
        #create labels and buttons
        self.title_label = Label(self.test_top, text="Testing State", font=("Arial", 16), width=50, borderwidth=5)
        self.calibration_button = Button(self.test_top, padx = 50, pady = 50, text="Calibrate the Motor", command=self.calibrate)
        self.time_test_button = Button(self.test_top, padx = 50, pady = 50, text="Time Test the Motor", command=self.time_test)

        #place labels and buttons
        self.title_label.grid(row=0,column=0, columnspan=3)
        self.calibration_button.grid(row=2,column=0, padx = (25,25), pady=(100,100))
        self.time_test_button.grid(row=2,column=2, padx = (25,25), pady=(100,100))
        
        
       
        
        
        
        
    #send a MQTT Message to calbrate the Machine 
    def calibrate(self):
        self.client.publish("tuf53905@temple.edu/MotorControl", "calibrate")
        self.calibration_complete = "complete"
       
#         testing = 0
#         self.client.start_loop()
#         while (testing == 0):
#             self.client.publish("tuf53905@temple.edu/MotorControl", "calibrate")
#             self.client.wait_for_publish()
#             print(self.client.is_published())
#             if (self.client.is_published()):
#                 testing = 1
#                 self.client.stop_loop()
        return("calibration complete")
    
    def time_test(self):
        self.client.publish("tuf53905@temple.edu/MotorControl", "testing")
        self.calibration_complete = "complete"
        return 
        
        
            
        
        
        
        
        