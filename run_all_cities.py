import os 
import sys
import re 
import glob 

# foo.csv --> any CSV file name 
# run commmand ... python run_all_cities.py > foo.csv
def main():
	headers = ['city', 'state', 'category', 'tier', 'urban_population', 'population_growth', 'working', 'area', 'density', 'youth', 'slum', 'tribes', 'literacy', 'population', 'caste', 'working-participation', 'per_capita', 'unemployment', 'work-agriculture', 'work-technicians', 'work-machine-operators', 'work-service', 'work-clerks', 'work-craft', 'work-professionals', 'work-legislators', 'electricity', 'mobile-ownership', 'type-waste', 'tap-water', 'no-internet-computer', 'internet-computer', 'toilet-on-premise', 'connected-drainage', 'housing-owned', 'school-primary-per', 'school-college-per', 'housing-congested', 'school-middle-per', 'school-secondary-per', 'hospital-per', 'housing-rented']
	print ",".join(headers)
	# all_files = os.listdir('./TXT')
	all_csv = glob.glob('./CSV/*.csv')


	# print all_csv
	for entry in all_csv:
		string = "python city_extract_csv.py " + entry
		os.system(string)

if __name__ == "__main__":
    main()