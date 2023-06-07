import re
def sum_of_a_beach(beach):
	beach = beach.lower()
	match = ["Sand","Water","Fish","Sun"]
	match2 = []
	results = []
	summation = 0
	for x in match:
		match2.append(x.lower())
	for j in match2:
		results.append(beach.count(j))
	
	for i in results:
		summation += i
	return summation
"""	
-----------Best Solution-------
	return len(re.findall('Sand|Water|Fish|Sun', beach, re.IGNORECASE))
"""
print sum_of_a_beach("sunsunsunsun")
