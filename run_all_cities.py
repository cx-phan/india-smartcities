import os 
import sys
import re 

# def convertToFile():
# 	command = "curl -F f=@example.pdf \"https://pdftables.com/api?key=yo14ql1qna09&format=xlsx-single\""
# def writeToTSV(): 

def main():
	# sys.stdout = open('file.txt', 'w')
	
	headers = ['city', 'state', 'category', 'tier', 'urban_population', 'population_growth', 'working', 'area', 'density', 'youth', 'slum', 'tribes', 'literacy', 'population', 'caste', 'unemployment', 'per_capita', 'working', 'workstatus', 'professionals', 'legislators', 'service', 'machine-operators', 'technicians', 'craft', 'clerks', 'agriculture']
	print ",".join(headers)
	all_files = os.listdir('./TXT')
	all_csv = os.listdir('./CSV/')



	for entry in all_csv:
		print entry
		string = "python city_extract_csv.py ./CSV/" + entry
		os.system(string)

if __name__ == "__main__":
    main()