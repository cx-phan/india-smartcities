import os 
import sys
import re 

# functions for debugging
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

def toCSV(city, state, category, tier, city_stat, employment_stat, industry_stat, infrastructure_stat):
	headers = ['city', 'state', 'category', 'tier'] + city_stat.keys() + employment_stat.keys() + industry_stat.keys() + infrastructure_stat.keys()
	values = [city, state, category, tier] + city_stat.values() + employment_stat.values() + industry_stat.values() + infrastructure_stat.values()
	print ",".join(values)

def writeDictionary(dictionary, data): 
	dict2 = {}
	for key in dictionary.keys(): 
		pattern = dictionary[key]
		temp = re.findall(pattern, data)
		# print pattern
		# print temp

		if len(temp) > 0:
			length = len(temp[0])
			if type(temp[0]) == tuple:
				dict2[key] = temp[0][length-1].encode('utf-8')
			else:
				dict2[key] = temp[0].encode('utf-8')
		else:
			dict2[key] = 'N/A'

	# print dict2
	return dict2

def infras(data):
	infrastructure = {}
	infrastructure_stat = {}

	infrastructure['tap-water'] = "\"% of households with access to tap water\n?(treated )?source\) within Premises\",\(from( treated)?,([0-9.]+)"
	infrastructure['electricity'] = "% of households with access to electricity,+([0-9.]+)"
	infrastructure['toilet'] = "\"?% of households having toilet facilities within\n?premises\"?,+([0-9.]+)"
	infrastructure['drainage'] = "\"% of household Waste water outlet connected to\n?drainage\",+([0-9.]+)"
	# should include? look again for review 
	infrastructure['sewerage'] = "Type of sewerage system\*,+\"([\w\n ]+)\""
	infrastructure['type'] = "Type of solid Waste system\*,+([\w\n ]+)"
	infrastructure['mobile-ownership'] = "% of households with access to mobile phones,+([0-9.]+)"
	infrastructure['internet-computer'] = "\"?% of households with access to computer\/laptop\nwith internet\n?without internet\",+\"?([0-9.]+)\n[0-9.]+"
	infrastructure['no-internet-computer'] = "\"?% of households with access to computer\/laptop\nwith internet\n?without internet\",+\"?[0-9.]+\n([0-9.]+)"
	infrastructure['housing-owned'] = "Owned\nRented\",+\"([0-9.]+)\n[0-9.]+"
	infrastructure['housing-rented'] = "Owned\nRented\",+\"[0-9.]+\n([0-9.]+)"
	
	infrastructure_stat = writeDictionary(infrastructure, data)
	return infrastructure_stat

def industry(data):

	industry = {} 
	industry_stat = {}
	industry['legislators'] = "\"Legislators, senior officials and managers\",+([0-9.]+)"
	industry['professionals'] = "\"?Professionals\"?,+([0-9.]+)"
	industry['technicians'] = "\"?Technicians and associate professionals\"?,+([0-9.]+)"
	industry['clerks'] = "\"?Clerks\"?,+([0-9.]+)"
	industry['service'] = "\"?Service workers and shop and market sales ?\n?workers\"?,+([0-9.]+)"
	industry['agriculture'] = "\"?Skilled agricultural and fishery workers\"?,+([0-9.]+)"
	industry['craft'] = "\"?Craft and related trades workers\"?,+([0-9.]+)"
	industry['machine-operators'] = "\"?Plant and machine operators and\n? ?assemblers\"?,+([0-9.]+)"
	industry_stat = writeDictionary(industry, data)
	return industry_stat

# employment statistics 
def employmentstats(data):
	# print "==== EMPLOYMENT===="
	employment = {}

	employment['per_capita'] = "Per Capita Income \(Rs.?\) at 2004-05 \D*([0-9]+)"
	employment['unemployment'] = "\"Unemployment Rate, 2011-12\*\*\*\",([0-9.]+)"
	employment['working'] = "\"Work Participation Rate, 2011-12\*\*\*\",([0-9.]+)"

	emp_stat = writeDictionary(employment, data)

	return emp_stat

# stats drawn on India Census 
def citystats(data):
	# print " === CITY CENSUS ===="
	city_text = {} 
	city_stat = {}
	# stats on population 

	city_text['population'] = "Total Population,\"?([0-9]+)\"?"
	city_text['urban_population'] = "Total Population of UA \(if\)\,\"?([0-9]+)\"?"
	city_text['population_growth'] = "Population Growth Rate \(AEGR\) 2001-11,([-0-9.]+)"
	city_text['area'] = "Area \(sq\. km\)\*,([0-9.]+)"
	city_text['density'] = "Density of population \(person per sq\. km\)\*,([0-9]+)"
	
	# more stats on city characteristics, India Census 
	city_text['literacy'] = "Literacy Rate \(%\),([0-9\.]+)"
	city_text['caste'] = "Schedule Caste \(%\),([0-9\.]+)"
	city_text['tribes'] = "Schedule Tribes \(%\),([0-9\.]+)"
	city_text['youth'] = "Youth, ?15 ?- ?24 ?years ?\(%\)\",([0-9\.]+)"
	city_text['slum'] = "Slum Population \(%\),([0-9\.]+)"
	city_text['working'] = "\"?Working Age Group, 15-59 years \(%\)\"?,([0-9\.]+)"

	city_stat = writeDictionary(city_text, data)

	return city_stat

	
def cities(data):
	city = re.findall('City: (\w+)', data)[0].encode('utf-8')
	state = re.findall('State: (\w+ ?\w+)', data)[0].encode('utf-8')
	category_tier_search = "Category: ([.\s\S]+?), Tier ([0-9])"
	category, tier = re.findall(category_tier_search, data)[0]
	return city, state, category.encode('utf-8'), tier.encode('utf-8')

def main(): 

	filename = sys.argv[1]

	with open(filename, "r") as myfile:
  		data = myfile.read().decode('utf-8')

  	city, state, category, tier = cities(data)
  	city_stat = citystats(data)
  	employment_stat = employmentstats(data)
  	industry_stat = industry(data)
  	infrastructure_stat = infras(data)
  	toCSV(city, state, category, tier, city_stat, employment_stat, industry_stat, infrastructure_stat)
	
if __name__ == "__main__":
    main()