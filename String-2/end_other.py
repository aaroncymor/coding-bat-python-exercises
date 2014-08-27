"""
	
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences 
(in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string. 
"""

def end_other(a, b):
	small_a = a.lower()
	small_b = b.lower()
	
	if len(small_a) > len(small_b):
		if small_a[-len(small_b):] == small_b:
			return True
	elif len(small_a) < len(small_b):
		if small_b[-len(small_a):] == small_a:
			return True
	elif len(small_a) == len(small_b):
		if small_a == small_b:
			return True
	return False
	"""
	if len(small_a) > len(small_b):
		#code here
		for i in range(len(small_a[len(small_b)-1:])):
			if small_a[i:i+len(small_b)] == small_b:
				if 
				return True
	elif len(small_a) < len(small_b):
		for i in range(len(small_b[len(small_a)-1:])):
			if small_b[i:i+len(small_a)] == small_a:
				return True		
	elif len(small_a) == len(small_b):
		if small_a == small_b:
			return True
	return False
	"""

print end_other('Hiabc','abc')
"""
 a b x a b c
0 1 2 3 4 5 6
6 5 4 3 2 1
"""