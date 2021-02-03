import RPi.GPIO as GPIO

class Idle:
    
    def __init__(self):
        self.idle_top = Toplevel()
        self.idle_top.title("Idle")

        #create stop button
        stop_button = Button(idle_top, text="STOP IDLE", command=self.stop_idle)
        stop_button.grid(row=1,column=0,columnspan=2)



        
        self.idle_stop = 1

            
    def wait_for_signal(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        while idle_stop != 0:
            GPIO.add_event_detect(25, GPIO.FALLING, callback=self.call_25, bouncetime=300)
            GPIO.add_event_detect(16, GPIO.FALLING, callback=self.call_16, bouncetime=300)
            

            
    def call_25(self, channel):
        call_floor_25 = Floor(25)
        call_floor_25.send_message()
        print('whats better than 24?')
        return
    
    def call_16(self, channel):
        call_floor_16 = Floor(16)
        call_floor_16.send_message()
        print('called')
        return
    
    def stop_idle(self):
        GPIO.cleanup()
        self.idle_stop = 0
        self.idle_top.destroy()
        return


