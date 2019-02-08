import os 
import sys
import re 

def industry(data):
	print "==== CITY INDUSTRY ==== "

	industry = {} 
	industry_stat = {}
	industry['legislators'] = "\"Legislators, senior officials and managers\",+([0-9.]+)"
	industry['professionals'] = "\"?Professionals\"?,+([0-9.]+)"
	industry['technicians'] = "\"?Technicians and associate professionals\"?,+([0-9.]+)"
	industry['clerks'] = "\"?Clerks\"?,+([0-9.]+)"
	industry['service'] = "\"?Service workers and shop and market sales ?\n?workers\"?,([0-9.]+)"
	industry['agriculture'] = "\"?Skilled agricultural and fishery workers\"?,+([0-9.]+)"
	industry['craft'] = "\"?Craft and related trades workers\"?,+([0-9.]+)"
	industry['machine-operators'] = "\"?Plant and machine operators and assemblers\"?,+([0-9.]+)"

	for key in industry.keys(): 
		pattern = industry[key]

		temp = re.findall(pattern, data)
		if key == 'service':
			print "TEST >>> ", temp
			print industry[key]
		if len(temp) > 0:
			industry_stat[key] = temp[0]

		print key, temp

# employment statistics 
def employmentstats(data):
	print "==== CITY EMPLOYMENT ===="
	employment = {}

	employment['per_capita'] = "Per Capita Income \(Rs.?\) at 2004-05 \D*([0-9]+)"
	employment['unemployment'] = "\"Unemployment Rate, 2011-12\*\*\*\",([0-9.]+)"
	employment['working'] = "\"Work Participation Rate, 2011-12\*\*\*\",([0-9.]+)"
	employment['workstatus'] = "Work Status, 2011-12 \(%\) ([0-9.]+)"

	emp_stat = {}
	for key in employment.keys():
		pattern = employment[key]
		temp = re.findall(pattern, data)
		if len(temp) > 0:
			emp_stat[key] = temp[0]

		print key, temp

# stats drawn on India Census 
def citystats(data):
	print " === CITY CENSUS ===="
	city_text = {} 
	city_stat = {}
	# stats on population 

	city_text['population'] = "Total Population,\"([0-9,]+)\""
	city_text['urban_population'] = "Total Population of UA \(if\)\,\"([0-9,]+)\""
	city_text['population_growth'] = "Population Growth Rate \(AEGR\) 2001-11,([0-9.]+)"
	city_text['area'] = "Area \(sq\. km\)\*,([0-9.]+)"
	city_text['density'] = "Density of population \(person per sq\. km\)\*,([0-9]+)"
	
	# more stats on city characteristics, India Census 
	city_text['literacy'] = "Literacy Rate \(%\),([0-9\.]+)"
	city_text['caste'] = "Schedule Caste \(%\),([0-9\.]+)"
	city_text['tribes'] = "Schedule Tribes \(%\),([0-9\.]+)"
	city_text['youth'] = "Youth, ?15 ?- ?24 ?years ?\(%\)\",([0-9\.]+)"
	city_text['slum'] = "Slum Population \(%\),([0-9\.]+)"
	city_text['working'] = "Working Age Group, 15-59 years \(%\),([0-9\.]+)"

	for key in city_text.keys():
		pattern = city_text[key]
		temp = re.findall(pattern, data)
		if len(temp) > 0: 
			city_stat[key] = temp[0]

		print key, temp

	# print population
	
def city(data):
	print "==== CITY STATISTICS ===== "
	city = re.findall('City: (\w+)', data)
	state = re.findall('State: (\w+ ?\w+)', data)
	category_tier_search = "Category: ([.\s\S]+?), Tier ([0-9])"
	category, tier = re.findall(category_tier_search, data)[0]
	print city, state
	print category, tier

def main(): 
	print "==== NEW CITY ======= "
	filename = sys.argv[1]

	with open(filename, "r") as myfile:
  		data = myfile.read().decode("utf-8")

  	city(data)
  	citystats(data)
  	employmentstats(data)
  	industry(data)
	
if __name__ == "__main__":
    main()