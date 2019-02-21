import requests
import os 
import sys
import re 
import glob 

def main():
	filename = 'city-wise.html'
	with open(filename, "r") as myfile:
  		data = myfile.read().decode('utf-8')

  	pattern = "([0-9]+)\.?<\/td>\n\t\t\t<td>\n\t\t\t\t<a href=\"(http:\/\/smartcities\.gov\.in\/upload\/uploadfiles\/files\/(.*)\.pdf)"
	results = re.findall(pattern, data)
	
	print requests.get('http://smartcities.gov.in/upload/uploadfiles/files/BMC_projects.pdf')
	for result in results:
		url = result[1]
		r = requests.get(url)

		# print r.url, r.text, r.content
		file_name = result[0] + '-' + result[2] + '.pdf'
		open(file_name, 'wb').write(r.content)
		continue

		print "Written\n"

if __name__ == "__main__":
    main()