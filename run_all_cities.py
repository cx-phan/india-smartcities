import os 
import sys
import re 

def main():
	all_files = os.listdir('./TXT')
	all_csv = os.listdir('./CSV/')
	print all_csv

	for entry in all_csv:
		string = "python city_extract_csv.py ./CSV/" + entry
		print string  
		os.system(string)

if __name__ == "__main__":
    main()