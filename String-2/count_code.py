"""
	
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count. 
"""

def count_code(str):
	i = 0
	code_ctr = 0
	while i <= len(str) - 4:
		if str[i:i+2] == "co":
			if str[i + 3] == "e":
				code_ctr += 1
		i += 1
	return code_ctr

print count_code('cozexxcope')
	