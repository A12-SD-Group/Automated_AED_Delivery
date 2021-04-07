from tkinter import *
from PIL import ImageTk,Image
#needed to use messagebox
from tkinter import messagebox
#from tkinter.ttk import Label
from initializing import Initialize
#from testing import *
#from active_running import *
import RPi.GPIO as GPIO
from floor import *
import signal
from idle import Idle
from Data_class import *
from testing_state import *

class AED_GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x400')
        self.title("Automated AED Delivery System")
        self.status=StringVar()
        self.status="Not Initialize"
        self.motor_calibration = "Motor Needs Calibration"
        
        #add labels 
        self.welcome_label = Label(self, text="Welcome to the Automated AED Delivery System", font=("Arial", 25), width=50, borderwidth=5)
        self.status_label = Label(self,text=self.status, font=("Arial", 16))
        self.welcome_label.grid(row=0,column=0, columnspan=3)
        self.status_label.grid(row=1,column=0,columnspan = 3, pady = 10)
        
        # #define buttons
        self.idle_button = Button(self, padx = 50, pady = 50, text="Idle State", command=self.idle_call)
        self.test_button = Button(self, padx = 50, pady = 50, text="Testing State", command=self.test_call)
        self.initialize_button = Button(self, padx = 50, pady = 50, text="Initializing State", command=self.init_call)

        self.idle_button.grid(row=2,column=0, padx = (25,0), pady=(0,100))
        self.test_button.grid(row=2,column=2, padx = (0,25), pady=(0,100))
        self.initialize_button.grid(row=2,column=1, padx = (25,25), pady=(0,100))
        
        self.init_data = None
        
        return 

    # #called when test button is hit in root
    def test_call(self):
        #change status of the label in root
        self.status = "Testing State"
        self.status_label.config(text=self.status)
        ########calls the MQTT as of right now
        #######testing_called()
        if(self.motor_calibration == "Motor Needs Calibration"):
            testing_window = Testing()
            self.wait_window(testing_window.test_top)
            self.motor_calibration = testing_window.calibration_complete
            del testing_window
        else:
            testing_window = Testing("complete")
            self.wait_window(testing_window.test_top)
            print("complete")
            del testing_window
            
        return 


    #called when initialze button is called in root window
    def init_call(self):
        self.status = "Initializing State"
        self.status_label.config(text=self.status)
        initialize_window = Initialize()
        self.wait_window(initialize_window.init_top)
        self.init_data = initialize_window.data_class.file_name
        del initialize_window
        return
    

    #function called with Idle State Button is Pressed
    def idle_call(self):
        if (self.motor_calibration == "Motor Needs Calibration"):
            messagebox.showerror("Motor Error", "You must calibrate the motor in the testing state before moving to the idle state.")
        else:
            #change status on main window
            self.status = "Idle State"
            self.status_label.config(text=self.status)
            #initiate idle state
            idle_window = Idle(self.init_data)
            self.wait_window(idle_window.idle_top)
            
            #destroy instance of Idle class when Idle is exited
            #remove interrupts
            del idle_window
            GPIO.remove_event_detect(25)
            GPIO.remove_event_detect(16)
            
        return

def main():
    global root
    root = AED_GUI()
    root.mainloop()
    
if __name__ == "__main__":
    main()
    