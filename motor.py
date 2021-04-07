import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setwarnings(False)
        
        self.ControlPin = [4,17,27,22]
        self.return_code = 0
        
        for pin in self.ControlPin:
            #GPIO.cleanup(pin)
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin,0)
            
        self.forward_seq = [[1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1], [1,0,0,1]]
        self.backward_seq = [[1,0,0,1], [0,0,0,1], [0,0,1,1], [0,0,1,0], [0,1,1,0], [0,1,0,0], [1,1,0,0], [1,0,0,0]]
    
    def go_24(self): 
        for i in range (0, 384):
            for halfstep in range(8):
                for pin in range(4):
                    ##set each pin ##
                    GPIO.output(self.ControlPin[pin], self.forward_seq[halfstep][pin])
                time.sleep(0.001)
        time.sleep(2)
        for i in range (0, 384):
            for halfstep in range(8):
                for pin in range(4):
                    ##set each pin ##
                    GPIO.output(self.ControlPin[pin], self.backward_seq[halfstep][pin])
                time.sleep(0.001)
                

    def go_16(self): 
        for i in range (0, 256):
            for halfstep in range(8):
                for pin in range(4):
                    ##set each pin ##
                    GPIO.output(self.ControlPin[pin], self.forward_seq[halfstep][pin])
                time.sleep(0.001)
        time.sleep(2)
        for i in range (0, 256):
            for halfstep in range(8):
                for pin in range(4):
                    ##set each pin ##
                    GPIO.output(self.ControlPin[pin], self.backward_seq[halfstep][pin])
                time.sleep(0.001)
                
## testing
def main():
    motor = Motor()
    motor.go_24()
    
    
if __name__ == "__main__":
    main()
    