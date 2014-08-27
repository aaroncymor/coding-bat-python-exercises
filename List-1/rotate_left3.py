"""
	Given an array of ints length 3, return an array with the elements "roted left so {1, 2, 3} yields
	{2,3,1}
"""
"""
def rotate_left3(nums):
	if len(nums) == 3:
		for i in range(len(nums)):
			nums[i] = 
	return nums
"""

def rotate_left3(nums):
	new_nums = []
	if len(nums) == 3:
		new_nums.append(nums[1])
		new_nums.append(nums[2])
		new_nums.append(nums[0])
	return new_nums
