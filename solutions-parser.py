import os 
import sys
import re 
import csv

# write the same information, but in binary form for easy grouping in Excel/Google Sheets
def write_to_file_two(city_dictionary, titles):
	newfile = "solutions-binary.tsv"

 	# return
	with open(newfile, 'w') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter='\t',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    spamwriter.writerow(["Name"] + titles)

	    for value in city_dictionary.keys():
	    	has_event = []
	    	for title in titles:
	    		has_event.append(title in city_dictionary[value])

	    	spamwriter.writerow([value] + has_event)

# write information in: name of city: projects format 
def write_to_file_one(city_dictionary):
	# do something here 
	newfile = "solutions-group.tsv"

	with open(newfile, 'w') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter='\t',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    for value in city_dictionary.keys():
	    	reply = ",".join(city_dictionary[value])
	    	spamwriter.writerow([value] + [reply])



def main(): 
	filename = "solutions-original-CSV.csv"
	city_dictionary = {} 
	all_jobs = set()
	with open(filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for i, row in enumerate(spamreader):
			if i == 0:
				continue
			all_cities = row[2:len(row)-2]
			activity = row[1]

			for city in all_cities:
				name = city.strip("\" ")
				if name in city_dictionary.keys():
					city_dictionary[name] += [activity]
				elif name == "":
					continue
				else: 
					city_dictionary[name] = [activity]
				all_jobs.add(activity.strip("\""))
	
	write_to_file_one(city_dictionary)
	write_to_file_two(city_dictionary, list(all_jobs))


if __name__ == "__main__":
    main()