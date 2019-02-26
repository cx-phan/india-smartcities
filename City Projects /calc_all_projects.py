# will calculate number of and all projects per city, per section 
import glob 
import os 
import re 
import csv
import numpy as np 

all_values = np.empty((21,31), dtype=object)

def parse(i, sort_CSV): 
	number_projects = {}
	money_projects = {}
	with open(sort_CSV, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for i, row in enumerate(spamreader):
			if i == 0 or i == 1:
				continue
			
			cost = 0.0

			if len(row[2]) > 0 and row[2] != '-':
				cost = float(row[2])


			if row[6] not in number_projects.keys():
				number_projects[row[6]] = 1
				money_projects[row[6]] =cost
			else:
				number_projects[row[6]] += 1
				money_projects[row[6]] += cost

	print "==== TEST ====== "
	print sort_CSV
	for j, proj in enumerate(number_projects.keys()):
		print proj
		print "Number: " + str(number_projects[proj])
		print "Crores: " + str(money_projects[proj])




	print "==== TEST ====== "




all_names = glob.glob('CSV-files/round-1/*.csv')
# print pattern
print len(all_names)

for i, name in enumerate(all_names):
	parse(i, name)
	all_values[i + 1][0] = name

print all_values

