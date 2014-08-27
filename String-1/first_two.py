"""
	Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the
	string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string ""
	yields an empty string "".
"""
def first_two(str):
	if len(str) < 2:
		return str
	elif len(str) >= 2:
		return str[0:2]