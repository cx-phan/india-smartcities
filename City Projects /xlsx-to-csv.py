import xlrd
import csv
import glob 
import os 
import re 

def convert_to_csv(name, new_name): 
	wb = xlrd.open_workbook(name)
	sh = wb.sheet_by_name('Table 1')
	your_csv_file = open(new_name, 'w')
	wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
	for rownum in range(sh.nrows):
		stripped = sh.row_values(rownum)
		for i, value in enumerate(stripped):
			# print value, type(value)
			if type(value) is unicode:
				stripped[i] = value.encode('ascii', 'ignore')
		wr.writerow(stripped)

	your_csv_file.close()


def csv_from_excel(name):
	string = './' + name + '/*.xlsx'
	pattern = '.\/round-[0-9]\/(.*?)\.xlsx'
	all_names = glob.glob(string)
	for nm in all_names:
		print nm
		str2 = re.findall(pattern, nm)[0]
		new_nm = './CSV-files/' + name + '/' + str2 + '.csv'
		convert_to_csv(nm, new_nm)
		continue

# runs the csv_from_excel function:

def main():
	all_names = ['round-1', 'round-2', 'round-3', 'round-4', 'round-5']
	os.system('mkdir CSV-files')
	for name in all_names:
		csv_from_excel(name)

if __name__ == "__main__":
    main()