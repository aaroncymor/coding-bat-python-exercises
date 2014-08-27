"""
	Return True if the given string contains an appearance of "xyz" where 
	the xyz is not directly preceeded by a period (.). So "xxyz" counts but 
	"x.xyz" does not. 
"""

def xyz_there(str):
	i = 0
	while i < len(str):
		if str[i: i+3] == 'xyz':
			if i > 0:
				if str[i - 1] != '.':
					return True
			elif i == 0:
				return True
		i += 1
	return False