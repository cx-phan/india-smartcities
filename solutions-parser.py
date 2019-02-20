import os 
import sys
import re 
import csv

def write_to_file(city_dictionary):
	# do something here 
	newfile = "testfile.csv"

	with open(newfile, 'w') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    for value in city_dictionary.keys():
	    	spamwriter.writerow([value] + city_dictionary[value])



def main(): 
	filename = "solutions.csv"
	city_dictionary = {} 
	with open(filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for i, row in enumerate(spamreader):
			if i == 0:
				continue
			# print len(row)
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
				# print name
	
	for value in city_dictionary.keys():
		print value, city_dictionary[value]
		print "\n"

	print sorted(city_dictionary.keys())
	write_to_file(city_dictionary)


if __name__ == "__main__":
    main()