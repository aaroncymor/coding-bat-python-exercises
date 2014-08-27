"""
	Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle
	elements.
"""

def middle_way(a,b):
	mid_list = []
	if len(a) == 3 and len(b) == 3:
		mid_list.append(a[1])
		mid_list.append(b[1])
	return mid_list
	