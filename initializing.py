import os
import datetime
import csv
from tkinter import *
from PIL import ImageTk,Image
#needed to use messagebox
from tkinter import messagebox
from Data_class import *


class Initialize:
    def __init__(self):
        #initalize data class
        self.data_class = None
        
        #call top window
        self.init_top = Toplevel()
        self.init_top.title("Initialization")
        
        #create prompt labels
        self.title_init = Label(self.init_top, text = "Please Enter Your Information", pady = 10)
        self.company_prompt = Label(self.init_top, text="Enter Name of Company: ", pady = 5)
        self.street_prompt = Label(self.init_top, text="Enter Street Address: ", pady = 5)
        self.city_prompt = Label(self.init_top, text="Enter City: ", pady = 5)
        self.state_prompt = Label(self.init_top, text="Enter State: ", pady = 5)
        self.zip_prompt = Label(self.init_top, text="Enter Zip Code: ", pady = 5)
        
        #place prompt labels
        self.title_init.grid(row=0, column = 0, columnspan = 2)
        self.company_prompt.grid(row = 1 , column = 0 , sticky=W)
        self.street_prompt.grid(row = 2, column = 0,sticky=W )
        self.city_prompt.grid(row = 3, column = 0, sticky=W)
        self.state_prompt.grid(row = 4, column = 0, sticky=W)
        self.zip_prompt.grid(row = 5, column = 0, sticky=W)
        
        
        #create entries 
        #global company_entry,street_entry, city_entry, state_entry, zip_entry
        self.company_entry = Entry(self.init_top, width = 50)
        self.street_entry = Entry(self.init_top, width = 50)
        self.city_entry = Entry(self.init_top, width = 50)
        self.state_entry = Entry(self.init_top, width = 50)
        self.zip_entry = Entry(self.init_top, width = 50)
        
        #place entries
        self.company_entry.grid(row = 1, column = 1, sticky=E)
        self.street_entry.grid(row = 2, column = 1, sticky=E)
        self.city_entry.grid(row = 3, column = 1, sticky=E)
        self.state_entry.grid(row = 4, column = 1, sticky=E)
        self.zip_entry.grid(row = 5, column = 1, sticky=E)
        
        #create button
        self.save_button = Button(self.init_top, text="Save", command=self.save_info)
        self.save_button.grid(row=6,column=0,columnspan=2)
        
        

    def save_info(self):
        company_name = self.company_entry.get()
        street_name = self.street_entry.get()
        city_name = self.city_entry.get()
        state_name = self.state_entry.get()
        zip_name = self.zip_entry.get()
        
        info_array = [company_name, street_name, city_name, state_name, zip_name]
        self.data_class = Data_class(info_array)
        
        exit_prompt = Label(self.init_top, text = "Save Complete, Please Close Window", pady = 10)
        exit_prompt.grid(row=6, column = 0, columnspan = 2)
        
        return
