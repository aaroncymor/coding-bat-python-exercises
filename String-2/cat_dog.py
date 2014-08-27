"""
	Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""

def cat_dog(str):
	cat_ctr = 0
	dog_ctr = 0
	i = 0
	while i <= len(str) - 1:
		if str[i:i+3] == "cat":
			cat_ctr += 1
		elif str[i:i+3] == "dog":
			dog_ctr += 1
		i += 1
	
	return (cat_ctr == dog_ctr)


print cat_dog('catdogdog')