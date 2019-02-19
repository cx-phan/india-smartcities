import os 
import sys
import re 
import csv


def main(): 
	filename = "solutions.csv"
	with open(filename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			print len(row)
			print row[2:len(row)-2]
			# print "What is this?" + row[len(row)-1]
			print row[1]


if __name__ == "__main__":
    main()