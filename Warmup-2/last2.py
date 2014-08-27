"""
	Given a string, return the count of the number of times that a substring length 2 appears in the
	string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end
	substring).
"""

def last2(str):
	ctr = 0
	last_two_char = str[-2:] 
	for i in range(len(str[:-2])):
		if last_two_char == str[i: i + 2]:
			ctr += 1
	return ctr