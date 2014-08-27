"""
	Given a string, return a new string where the first and las chars have been
	exchanged.
"""
code

def front_back(str):
	if len(str) == 1:
		return str
	elif len(str) > 1:
		return str[len(str) - 1] + str[1:len(str) - 1] + str[0]
	else:
		return None
		
"""
def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]
"""