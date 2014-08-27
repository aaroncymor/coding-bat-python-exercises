"""
	Given an array of ints, return the number of 9's in the array.
"""

def array_count9(nums):
	ctr = 0
	i = 0
	while i <len(nums):
		if nums[i] == 9:
			ctr += 1
		i += 1
	return ctr