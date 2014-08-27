"""
	Given an array of ints, return new array length 2 containing the first and last elements from the
	original array. The original array will be length 1 or more.
"""

def make_ends(nums):
	new_nums = []
	if nums > 1:
		new_nums.append(nums[0])
		new_nums.append(nums[-1])
	return new_nums