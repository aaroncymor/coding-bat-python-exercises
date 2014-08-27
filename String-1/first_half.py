"""
	Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
"""

def first_half(str):
	new_formed_str = ''
	m = len(str) / 2
	i = 0
	while i <= m - 1:
		new_formed_str += str[i]
		i += 1
	return new_formed_str