import os
import datetime
import csv
import paho.mqtt.client as mqtt 

class Floor:
    #this class connects to the MQTT and can send the emergency message though send_message function
    def __init__(self, floor_number):
        self.client = mqtt.Client("AED_rasp_pi")
        self.client.username_pw_set("tuf53905@temple.edu", password="GMPQTtw7")
        self.client.connect("maqiatto.com", 1883, 60 )
        self.message = "CARDIAC EMERGENCY ON FLOOR " + str(floor_number)
        self.floor_number = str(floor_number)
        return
    
    #sends the emergency message through the MaQiaTTo MQTT connection
    def send_message(self, location_message, floor):
        #input includes more specfic message with location
        sent_message = self.message + " at " + location_message
        self.client.publish("tuf53905@temple.edu/AEDAutoDelivery",sent_message)
        self.client.publish("tuf53905@temple.edu/MotorControl",floor)
        return
        
######Testing
# def main():
# 	test_floor = Floor(24)
# 	test_floor.send_message()
# 	return 
# 	
# 
# if __name__ == "__main__":
# 	main()
        