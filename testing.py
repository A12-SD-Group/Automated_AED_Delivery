
#!python3
import paho.mqtt.client as mqtt  #import the client1
import time

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
        
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

client = mqtt.Client("AED_rasp_pi")
client.on_connect = on_connect
client.on_publish = on_publish  
#client.on_message = on_message
#client.loop_start()
#client.connect("192.168.43.81", 1883, 60)
print("Connecting to broker ","maqiatto.com")
client.username_pw_set("tuf53905@temple.edu", password="GMPQTtw7")
client.connect("maqiatto.com", 1883, 60 )
client.publish("tuf53905@temple.edu/AEDAutoDelivery","on")                   #publish


client.loop_start()


while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in Main Loop")
client.loop_stop()    #Stop loop 
client.disconnect() # disconnect
