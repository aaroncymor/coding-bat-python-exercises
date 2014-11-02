"""
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- 
in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. 
Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for 
the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
Define the helper below and at the same indent level as the main no_teen_sum(). 
"""

def no_teen_sum(a,b,c):
	total = 0
	addends = []
	addends.append(a)
	addends.append(b)
	addends.append(c)
	for i in range(len(addends)):
		total += fix_teen(addends[i])
	
	return total
	
def fix_teen(num):
	if num in [13,14,17,18,19]:
		return 0
	elif num in [15,16]:
		return num
	else:
		return num
		
		
