import os 
import sys
import re 
import glob 

# foo.csv --> any CSV file name 
# run commmand ... python run_all_cities.py > foo.csv
def main():
	headers = ['city', 'state', 'category', 'tier', 'urban_population', 'population_growth', 'working', 'area', 'density', 'youth', 'slum', 'tribes', 'literacy', 'population', 'caste', 'per_capita', 'working', 'unemployment', 'professionals', 'legislators', 'service', 'machine-operators', 'technicians', 'craft', 'clerks', 'agriculture', 'housing-owned', 'toilet', 'electricity', 'mobile-ownership', 'tap-water', 'no-internet-computer', 'drainage', 'internet-computer', 'type-waste', 'housing-rented']
	print ",".join(headers)
	# all_files = os.listdir('./TXT')
	all_csv = glob.glob('./CSV/*.csv')


	# print all_csv
	for entry in all_csv:
		string = "python city_extract_csv.py " + entry
		os.system(string)

if __name__ == "__main__":
    main()