"""
	Given an array of ints length 3, return the sum of all the elements.
"""

def sum3(nums):
	total = 0
	if len(nums) == 3:
		for i in range(len(nums)):
			total += nums[i]
	return total