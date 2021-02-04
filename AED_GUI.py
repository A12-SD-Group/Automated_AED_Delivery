from tkinter import *
from PIL import ImageTk,Image
#needed to use messagebox
from tkinter import messagebox
#from tkinter.ttk import Label
from initializing import Initialize
from testing import *
#from active_running import *
import RPi.GPIO as GPIO
from floor import *
import signal
from idle import Idle
from Data_class import *

class AED_GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x400')
        self.title("Automated AED Delivery System")
        self.status=StringVar()
        self.status="Not Initialize"
        
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
        

    # #called when test button is hit in root
    def test_call(self):
        #change status of the label in root
        self.status = "Testing State"
        self.status_label.config(text=self.status)
        ###calls the MQTT as of right now
        testing_called()
        return 


    #called when initialze button is called in root window
    def init_call(self):
        self.status = "Initializing State"
        self.status_label.config(text=self.status)
        self.init_data = Initialize()
    

###########WHY YOU NO WORK########################
    def idle_call(self):
        self.status = "Idle State"
        self.status_label.config(text=self.status)
        self.idle_top = Toplevel()
        self.idle_top.title("Idle")
        #create exit label
        self.exit_idle_label = Label(self.idle_top, text="Exit the Window Idle Window to Exit Idle State")
        self.exit_idle_label.grid(row=0,column=0, columnspan=3, rowspan=3)
        idle_window = Idle(self.init_data.data_class.file_name)
        while idle_window.idle_stop == 1:
            pass
        print("I am out of while loop")
        del idle_window
        return

root = AED_GUI()

root.mainloop()

