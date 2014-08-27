"""
	Given a string and non-negative int n, return a larger 
	string that is n copies of the original string.
"""

def string_times(str, n):
	if str != '':
		if n > 0:
			return str * n