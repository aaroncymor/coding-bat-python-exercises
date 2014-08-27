"""
	Given a string, return a new string made of every other char starting with the
	first, so "Hello" yields "Hlo".
"""

def string_bits(str):
	new_formed_str = ''
	for i in range(len(str)):
		if i % 2 == 0:
			new_formed_str += str[i]
	return new_formed_str