"""
	Given a non-empty string like "Code" return a string like "CCoCodCode".
"""
def string_splosion(str):
	new_formed_str = ''
	i = 1
	while i <= len(str):
		new_formed_str += str[0:i]
		i += 1
	return new_formed_str