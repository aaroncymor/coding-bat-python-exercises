"""
	Return the number of times that the string "hi" appears anywhere in the given string.
"""

def count_hi(str):
	ctr = 0
	for i in range(len(str)):
		if str[i:i+2] == 'hi':
			ctr += 1
	return ctr