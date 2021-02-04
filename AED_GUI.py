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


#define root window
root = Tk()
root.title("Automated AED Delivery System")
#add an icon
#root.iconbitmap("@/home/pi/Automated_AED_System/temple_logo.ico")
img = PhotoImage(file='temple_logo.png')
root.tk.call('wm', 'iconphoto', root._w, img)

#state global variable delcaration 
#used in main window label to show active status
global status
status=StringVar()
status.set("Not Initialize")


#define button functions
#def idle_call():
	#change status of the label in root
#	status.set("Idle State")
#	status_label.config(text=status.get())
#	idle_state()
#	return

#called when test button is hit in root
def test_call():
	#change status of the label in root
	status.set("Testing State")
	status_label.config(text=status.get())
	###calls the MQTT as of right now
	testing_called()
	return 


#called when initialze button is called in root window
def init_call():
    status.set("Initializing State")
    status_label.config(text=status.get())
    init_data = Initialize()
    


def idle_call():
    idle_window = Idle(file_path)
    while idle_window.idle_stop != 0:
        idle_window.wait_for_signal()
        
    del idle_window
    
    return
    

#add labels 
welcome_label = Label(root, text="Welcome to the Automated AED Delivery System", font=("Arial", 25), width=50, borderwidth=5)
status_label = Label(root,text=status.get(), font=("Arial", 16))
welcome_label.grid(row=0,column=0, columnspan=3)
status_label.grid(row=1,column=0,columnspan = 3, pady = 10)
	
#define buttons
idle_button = Button(root, padx = 50, pady = 50, text="Idle State", command=idle_call)
test_button = Button(root, padx = 50, pady = 50, text="Testing State", command=test_call)
initialize_button = Button(root, padx = 50, pady = 50, text="Initializing State", command=init_call)

idle_button.grid(row=2,column=0, padx = (25,0), pady=(0,100))
test_button.grid(row=2,column=2, padx = (0,25), pady=(0,100))
initialize_button.grid(row=2,column=1, padx = (25,25), pady=(0,100))

# ~ def openwindow():
	# ~ #global variables are needed within the top level windows
	# ~ top = Toplevel()
	# ~ top.title("second window")
	# ~ #add an icon
	# ~ top.iconbitmap("C:/Users/User1/Documents/SENIOR DESIGN/Automated_AED_Delivery/temple_logo.ico")
	# ~ lbl = Label(top, text="Hello World").pack()
	# ~ btn2 = Button(top, text="close window", command=top.destroy).pack()

# ~ btn = Button(root, text="open second window", command=openwindow).pack()


root.mainloop()
