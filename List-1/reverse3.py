"""
	Given an array of ints length 3, return a new array with the elements in reverse order, so {1,2,3}
	becomes {3,2,1}
"""

def reverse3(nums):
	reversed_nums = []
	i = len(nums) - 1
	while i >= 0:
		reversed_nums.append(nums[i])
		i -= 1
	return reversed_nums