import xlrd
import csv
import glob 
import os 
import re 

def convert_to_csv(name, new_name): 
	all_labels = ['Governance', 'Identity & Culture', 'Education','Health','Safety & Security','Economy & Employment','Housing & Inclusiveness','Public Open Space','Mixed Land Use; Compactness','Power Supply','Transportation & Mobility','Assured Water Supply','Wastewater Management','Solid Waste Management', 'Reduced Pollution', 'Unknown']

	wb = xlrd.open_workbook(name)
	sh = wb.sheet_by_name('Table 1')
	your_csv_file = open(new_name, 'w')
	wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

	for rownum in range(sh.nrows):
		stripped = sh.row_values(rownum)
		for i, value in enumerate(stripped):

			if type(value) is unicode:
				stripped[i] = value.encode('ascii', 'ignore').strip(',')

		answer = ''
		
		if len(stripped[3]) != 0: 
			print 'Title:', stripped[1]
			print 'Category', stripped[3]
			response = int(raw_input("Type is?: "))
			answer = all_labels[response - 1]

		wr.writerow(stripped + [answer])

	your_csv_file.close()


def csv_from_excel(name):
	# one = './demo-test/test.xlsx'
	# two = './CSV-files/demo-test/test.csv'
	# convert_to_csv(one, two)
	# return
	print name 
	string = './' + name + '/*.xlsx'
	pattern = '.\/round-[0-9]\/(.*?)\.xlsx'
	all_names = glob.glob(string)
	all_names = all_names
	for nm in all_names:

		str2 = re.findall(pattern, nm)[0]
		print str2
		new_nm = './CSV-files/' + name + '/' + str2 + '.csv'
		convert_to_csv(nm, new_nm)

# runs the csv_from_excel function:

def main():
	all_names = ['round-1', 'round-2', 'round-3', 'round-4', 'round-5']
	# os.system('mkdir CSV-files')
	all_names = all_names[:1]
	for name in all_names:
		print name
		csv_from_excel(name)

if __name__ == "__main__":
    main()