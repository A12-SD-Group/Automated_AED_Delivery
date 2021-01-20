import os
import datetime
import csv


class Initialize:
	def __init__(self, data_array):
		#info_array = [company_name, street_name, city_name, state_name, zip_name]
		self.info_array = data_array
		
		#creates folder specifically for company
		path = os.getcwd()
		self.folder_name = path +"/" + data_array[0]
		if(not(os.path.exists(self.folder_name))):
			os.mkdir(self.folder_name)
		
		#grabs date information for csv file name
		temp_date = datetime.datetime.now()
		date = temp_date.strftime("%x")
		date = date.replace("/","_")
		
		#creates csv file
		self.file_name = self.folder_name + "/" + data_array[0] + "_info_" + date + ".csv"
		fields = ['company_name', 'street_name', 'city_name', 'state_name', 'zip_name']
		with open(self.file_name, 'w') as csvfile:
			
			csvwriter = csv.writer(csvfile)
			
			csvwriter.writerow(fields)
			csvwriter.writerow(self.info_array)
		

######Testing
def main():
	test = Initialize(["carly", "longo"])
	print(test.info_array)
	

if __name__ == "__main__":
	main()
