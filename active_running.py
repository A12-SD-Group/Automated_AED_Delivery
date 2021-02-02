import RPi.GPIO as GPIO
from floor import *
import signal


### ACTIVE STATE
GPIO.setmode(GPIO.BCM)

#GPIO.setup(16, GPIO.IN)
#GPIO.setup(25, GPIO.IN)

def call_16(channel):
    call_floor_16 = Floor(16)
    call_floor_16.send_message()
    print('called')
    return
    
def call_25(channel):
    call_floor_25 = Floor(25)
    call_floor_25.send_message()
    print('whats better than 24?')
    return

#GPIO.add_event_detect(25, GPIO.FALLING, callback=call_25, bouncetime=300)
#GPIO.add_event_detect(16, GPIO.FALLING, callback=call_16, bouncetime=300)



#### IDLE STATE
def idle_state():
    
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(25, GPIO.FALLING, callback=call_25, bouncetime=300)
    GPIO.add_event_detect(16, GPIO.FALLING, callback=call_16, bouncetime=300)
    
    
    #####need to figure out how to break this while loop 
    i = 0
    j=0
    while i != 1:
        try:
            while True:
                j=j+1
        except KeyboardInterrupt:
            i = 1
            print(i)
    return
    
    
    
            
