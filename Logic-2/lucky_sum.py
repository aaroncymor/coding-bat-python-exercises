"""
Given 3 int values, a b c, return their sum. 
However, if one of the values is 13 then it does not count towards the sum 
and values to its right do not count. So for example, if b is 13, then both b and c do not count. 
"""
def lucky_sum(a,b,c):
	addends = []
	addends.append(a)
	addends.append(b)
	addends.append(c)
	
	total = 0
	for i in range(len(addends)):
		if addends[i] == 13:
			break
		else:
			total +=addends[i]
	return total

	
