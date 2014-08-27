"""
	Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The
	string length will be at least 2.
"""
def extra_end(str):
	if len(str) == 2:
		return str * 3
	elif len(str) > 2:
		return str[len(str) - 2:len(str)] * 3
		

"""
	def extra_end(str):
		end = str[-2:]
		return end + end + end
"""