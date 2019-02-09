import os 
import sys
import re 

def toCSV(city, state, category, tier, city_stat, employment_stat, industry_stat):
	headers = ['city', 'state', 'category', 'tier'] + city_stat.keys() + employment_stat.keys() + industry_stat.keys()
	values = [city, state, category, tier] + city_stat.values() + employment_stat.values() + industry_stat.values()
	print ",".join(values)

def infras(data):
	infrastructure = {}
	infrastructure_stat = {}

	infrastructure['tap-water'] = "\"% of households with access to tap water\n(treated )?source\) within Premises\",\(from( treated)?,([0-9.]+)"

	for key in infrastructure.keys(): 
		pattern = infrastructure[key]
		print pattern
		temp = re.findall(pattern, data)
		print temp

		if len(temp) > 0:
			infrastructure_stat[key] = temp[len(temp)-1].encode('utf-8')
		else:
			infrastructure_stat[key] = 'N/A'

	print infrastructure_stat
	return infrastructure_stat

def industry(data):

	industry = {} 
	industry_stat = {}
	industry['legislators'] = "\"Legislators, senior officials and managers\",+([0-9.]+)"
	industry['professionals'] = "\"?Professionals\"?,+([0-9.]+)"
	industry['technicians'] = "\"?Technicians and associate professionals\"?,+([0-9.]+)"
	industry['clerks'] = "\"?Clerks\"?,+([0-9.]+)"
	industry['service'] = "\"?Service workers and shop and market sales ?\n?workers\"?,([0-9.]+)"
	industry['agriculture'] = "\"?Skilled agricultural and fishery workers\"?,+([0-9.]+)"
	industry['craft'] = "\"?Craft and related trades workers\"?,+([0-9.]+)"
	industry['machine-operators'] = "\"?Plant and machine operators and\n? ?assemblers\"?,+([0-9.]+)"

	for key in industry.keys(): 
		pattern = industry[key]

		temp = re.findall(pattern, data)

		if len(temp) > 0:
			industry_stat[key] = temp[0].encode('utf-8')
		else:
			industry_stat[key] = 'N/A'

	return industry_stat

# employment statistics 
def employmentstats(data):
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
			emp_stat[key] = temp[0].encode('utf-8')
		else:
			emp_stat[key] = 'N/A'

	return emp_stat

# stats drawn on India Census 
def citystats(data):
	# print " === CITY CENSUS ===="
	city_text = {} 
	city_stat = {}
	# stats on population 

	city_text['population'] = "Total Population,\"?([0-9]+)\"?"
	city_text['urban_population'] = "Total Population of UA \(if\)\,\"?([0-9]+)\"?"
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
			city_stat[key] = temp[0].encode('utf-8')
			# print key, city_stat[key]
		else:
			city_stat[key] = 'N/A'

	return city_stat

	
def cities(data):
	# print "==== CITY STATISTICS ===== "
	city = re.findall('City: (\w+)', data)[0].encode('utf-8')
	state = re.findall('State: (\w+ ?\w+)', data)[0].encode('utf-8')
	category_tier_search = "Category: ([.\s\S]+?), Tier ([0-9])"
	category, tier = re.findall(category_tier_search, data)[0]

	return city, state, category.encode('utf-8'), tier.encode('utf-8')

def main(): 
	# print "==== NEW CITY ======= "
	filename = sys.argv[1]

	with open(filename, "r") as myfile:
  		data = myfile.read().decode('utf-8')

  	city, state, category, tier = cities(data)
  	# city_stat = citystats(data)
  	# employment_stat = employmentstats(data)
  	# industry_stat = industry(data)
  	infrastructure_stat = infras(data)
  	# toCSV(city, state, category, tier, city_stat, employment_stat, industry_stat)
	
if __name__ == "__main__":
    main()