import os
import datetime
import csv
import paho.mqtt.client as mqtt 

class Floor:
    def __init__(self, floor_number):
        self.client = mqtt.Client("AED_rasp_pi")
        self.client.username_pw_set("tuf53905@temple.edu", password="GMPQTtw7")
        self.client.connect("maqiatto.com", 1883, 60 )
        self.message = "CARDIAC EMERGENCY ON FLOOR " + str(floor_number)
    def send_message(self):
        self.client.publish("tuf53905@temple.edu/AEDAutoDelivery",self.message)
        
######Testing
def main():
	test_floor = Floor(3)
	test_floor.send_message()
	

if __name__ == "__main__":
	main()
        