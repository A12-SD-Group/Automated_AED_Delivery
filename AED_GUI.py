from tkinter import *
from PIL import ImageTk,Image
#needed to use messagebox
from tkinter import messagebox
#from tkinter.ttk import Label
from initializing import Initialize


###testing commit

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
def idle_call():
	#change status of the label in root
	status.set("Idle State")
	status_label.config(text=status.get())	
	return

#called when test button is hit in root
def test_call():
	#change status of the label in root
	status.set("Testing State")
	status_label.config(text=status.get())
	return 

#function called after save button is push in init_call top level window
def save_info():
	company_name = company_entry.get()
	street_name = street_entry.get()
	city_name = city_entry.get()
	state_name = street_entry.get()
	zip_name = zip_entry.get()
	
	info_array = [company_name, street_name, city_name, state_name, zip_name]
	info_class = Initialize(info_array)
	
	return
	
#called when initialze button is called in root window
def init_call():
	#change status of the label in root
	status.set("Initializing State")
	status_label.config(text=status.get())
	
	#call top window
	init_top = Toplevel()
	init_top.title("Initialization")
	
	#create prompt labels
	title_init = Label(init_top, text = "Please Enter Your Information", pady = 10)
	company_prompt = Label(init_top, text="Enter Name of Company: ", pady = 5)
	street_prompt = Label(init_top, text="Enter Street Address: ", pady = 5)
	city_prompt = Label(init_top, text="Enter City: ", pady = 5)
	state_prompt = Label(init_top, text="Enter State: ", pady = 5)
	zip_prompt = Label(init_top, text="Enter Zip Code: ", pady = 5)
	
	#place prompt labels
	title_init.grid(row=0, column = 0, columnspan = 2)
	company_prompt.grid(row = 1 , column = 0 , sticky=W)
	street_prompt.grid(row = 2, column = 0,sticky=W )
	city_prompt.grid(row = 3, column = 0, sticky=W)
	state_prompt.grid(row = 4, column = 0, sticky=W)
	zip_prompt.grid(row = 5, column = 0, sticky=W)
	
	
	#create entries 
	global company_entry,street_entry, city_entry, state_entry, zip_entry
	company_entry = Entry(init_top, width = 50)
	street_entry = Entry(init_top, width = 50)
	city_entry = Entry(init_top, width = 50)
	state_entry = Entry(init_top, width = 50)
	zip_entry = Entry(init_top, width = 50)
	
	#place entries
	company_entry.grid(row = 1, column = 1, sticky=E)
	street_entry.grid(row = 2, column = 1, sticky=E)
	city_entry.grid(row = 3, column = 1, sticky=E)
	state_entry.grid(row = 4, column = 1, sticky=E)
	zip_entry.grid(row = 5, column = 1, sticky=E)
	
	#create button
	save_button = Button(init_top, text="Save", command=save_info)
	save_button.grid(row=6,column=0,columnspan=2)	
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
