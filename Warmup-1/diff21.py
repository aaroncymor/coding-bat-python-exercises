"""
	Given an int n, return the absolute difference between n and 21,
	except return double the absolute difference if n is over 21.
"""

def diff21(n):
	ans = n - 21
	if ans < 0:
		ans = ans * -1
	elif ans > 0:
		ans = ans * 2
	return ans