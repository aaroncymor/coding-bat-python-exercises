"""
	Given 3 int values, a b c, return their sum. However, if one of the values is the same as another
	of the values, it does not count towards the sum.
"""

def lone_sum(a, b, c):
	if a == b and b == c:
		return 0
	elif a == b and b != c:
		return c
	elif b == c and a != b:
		return a
	elif a == c and (a != b and b != c):
		return b
	else:
		return a + b + c
		
"""
Coding bat solution
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum
"""