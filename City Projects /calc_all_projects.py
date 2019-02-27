# will calculate number of and all projects per city, per section 
import glob 
import os 
import re 
import csv
import numpy as np 

all_values = np.empty((21,33), dtype=object)
all_labels = ['Governance', 'Identity & Culture', 'Education','Health','Safety & Security','Economy & Employment','Housing & Inclusiveness','Public Open Space','Mixed Land Use; Compactness','Power Supply','Transportation & Mobility','Assured Water Supply','Wastewater Management','Solid Waste Management', 'Reduced Pollution', 'Unknown']


def parse(index, sort_CSV): 
	number_projects = {}
	money_projects = {}
	with open(sort_CSV, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for i, row in enumerate(spamreader):
			if i == 0 or i == 1 or len(row[6]) == 0:
				continue
			
			cost = 0.0

			if len(row[2]) > 0 and row[2] != '-':
				cost = float(row[2])

			# print row[6], row[0]
			if row[6] not in number_projects.keys():

				number_projects[row[6]] = 1
				money_projects[row[6]] =cost
			else:
				number_projects[row[6]] += 1
				money_projects[row[6]] += cost

	
	for j, proj in enumerate(number_projects.keys()):
		value = all_labels.index(proj)
		number = str(number_projects[proj])
		money = str(money_projects[proj])
		# assign number
		all_values[index + 1][(value + 1)* 2 - 1] = number
		# assign money 
		all_values[index + 1][(value + 1) * 2] = money


	return number_projects



all_names = glob.glob('CSV-files/round-1/*.csv')
# print pattern

for i, name in enumerate(all_names):
	parse(i, name)
	all_values[i + 1][0] = name

for i, name in enumerate(all_labels): 
	all_values[0][(i + 1)* 2 - 1] = name + ' - Number'
	all_values[0][(i + 1)* 2] = name + ' - Money'

print all_values
np.savetxt("save_all_project_values.tsv", all_values, fmt='%s', delimiter="\t")

