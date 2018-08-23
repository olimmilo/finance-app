import csv
import sys
import pathlib

docuement_open = 0

while docuement_open == 0:
	open_page = input("Enter 'o' to open a docuement or 'n' to create a new docuement: ")
	if open_page == 'o':
		docuement_open = 1
		file_selected = 0
		while file_selected == 0:
			docuement_path = Path(input("Enter the path to your docuement from home(~): "))
			if document_path.is_file():
				print("File opened")
				file_selected = 1	
			else:
				print("File does not exist")			
	elif open_page == 'n':
		docuement_open = 1
		file_name = input("Enter a file name: ") + ".csv"
		new_file = open(file_name, 'a')
		file.close
	else:
		print("Invalid input, try again.)
