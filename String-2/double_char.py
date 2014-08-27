"""
	Given a string, return a string where for every char in the original,
	there are two chars.
"""

def double_char(str):
	temp = ''
	word = ''
	for i in range(len(str)):
		#if temp != str[i]:
			#temp = str[i]
		word += str[i] * 2
			#print temp
		
		#word += temp
	return word

"""
def double_char(str):
	if len(str) <= 1:
		return str
	else:
		first_char = str[0]
		ctr = 0
		i = 0
		while i <= len(str) - 1:
			if first_char == str[i]:
				ctr += 1
			i += 1
	body = str[ctr:]
	
	return first_char * (ctr * 2) + body
"""
	
print double_char("aaron")