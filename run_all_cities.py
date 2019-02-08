import os 
import sys
import re 
import glob 

# run commmand ... python run_all_cities.py > foo.csv
def main():
	
	headers = ['city', 'state', 'category', 'tier', 'urban_population', 'population_growth', 'working', 'area', 'density', 'youth', 'slum', 'tribes', 'literacy', 'population', 'caste', 'unemployment', 'per_capita', 'working', 'workstatus', 'professionals', 'legislators', 'service', 'machine-operators', 'technicians', 'craft', 'clerks', 'agriculture']
	print ",".join(headers)
	# all_files = os.listdir('./TXT')
	all_csv = glob.glob('./CSV/*.csv')


	# print all_csv
	for entry in all_csv:
		string = "python city_extract_csv.py " + entry
		os.system(string)

if __name__ == "__main__":
    main()