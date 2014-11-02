"""
We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use 
big bars before small bars. Return -1 if it can't be done.
"""

def make_chocolate(small, big, goal):
	small_used_ctr = 0
	while goal >= 5 and big > 0:
		goal -= 5
		big -= 1
	
	while goal > 0 and small > 0:
		goal -= 1
		small -= 1
		small_used_ctr += 1
	
	if goal > 0:
		return -1
	return small_used_ctr
			
print make_chocolate(4, 1, 9) 
print make_chocolate(4, 1, 10)
print make_chocolate(4, 1, 7) 
print make_chocolate(6, 2, 7) 
print make_chocolate(4, 1, 5) 
print make_chocolate(4, 1, 4) 
print make_chocolate(5, 4, 9) 
print make_chocolate(9, 3, 18)
print make_chocolate(3, 1, 9) 
print make_chocolate(1, 2, 7) 
print make_chocolate(1, 2, 6) 
print make_chocolate(1, 2, 5) 
print make_chocolate(6, 1, 10)
print make_chocolate(6, 1, 11)
print make_chocolate(6, 1, 12)
print make_chocolate(6, 1, 13)
print make_chocolate(6, 2, 10)
print make_chocolate(6, 2, 11)
print make_chocolate(6, 2, 12)
print make_chocolate(60, 100, 550)	    
print make_chocolate(1000, 1000000, 5000006)
print make_chocolate(7, 1, 12)	    
print make_chocolate(7, 1, 13)	    
print make_chocolate(7, 2, 13)	    
