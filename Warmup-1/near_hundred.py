"""
Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.
"""

def near_hundred(n):
	if (n <= 210 and n >= 190) or (n <= 110 and n >= 90):
		return True
	return False