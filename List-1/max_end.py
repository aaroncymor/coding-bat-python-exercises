"""
	Given an array of ints length 3, figure out which is larger between the first and last elements in the
	array, and set all the other elements to be that value. Return the changed array.
"""

def max_end3(nums):
	temp_max = 0
	new_nums = []
	if len(nums) == 3:
		if nums[0] >= nums[2]:
			temp_max = nums[0]
		elif nums[2] >= nums[0]:
			temp_max = nums[2]
					
		for i in range(3):
			new_nums.append(temp_max)
	return new_nums
	
max_end3([1,2,3])