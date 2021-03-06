"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.
"""

def make_bricks(small,big,goal):
	b_ctr = 0
	s_ctr = 0
	target = goal
		
	if big > 0:
		while target >= 5 and big > b_ctr:
			target -= 5
			b_ctr += 1
	
	if small > 0:
		while target > 0 and small > s_ctr:
			target -= 1
			s_ctr += 1
	
	if ((b_ctr * 5) + (s_ctr * 1)) == goal:
		return True
	return False

print str(make_bricks(3, 1, 8)) + " expected output: True"
print str(make_bricks(3, 1, 9)) + " expected output: False "
print str(make_bricks(3, 2, 10))+ " expected output:  True "
print str(make_bricks(3, 2, 8)) + " expected output: True	"
print str(make_bricks(3, 2, 9)) + " expected output: False "
print str(make_bricks(6, 1, 11))+ " expected output:  True "
print str(make_bricks(6, 0, 11))+ " expected output:  False"
print str(make_bricks(1, 4, 11))+ " expected output:  True "
print str(make_bricks(0, 3, 10))+ " expected output:  True "
print str(make_bricks(1, 4, 12))+ " expected output:  False"
print str(make_bricks(3, 1, 7)) + " expected output: True	"
print str(make_bricks(1, 1, 7)) + " expected output: False "
print str(make_bricks(2, 1, 7)) + " expected output: True	"
print str(make_bricks(7, 1, 11))+ " expected output:  True	"
print str(make_bricks(7, 1, 8)) + " expected output: True  "
print str(make_bricks(7, 1, 13)) + " expected output: False"
print str(make_bricks(43, 1, 46))+ " expected output: True	"
print str(make_bricks(40, 1, 46))+ " expected output: False"
print str(make_bricks(40, 2, 47))+ " expected output: True "
print str(make_bricks(40, 2, 50))+ " expected output: True "
print str(make_bricks(40, 2, 52))+ " expected output: False"
print str(make_bricks(22, 2, 33))+ " expected output: False"
print str(make_bricks(0, 2, 10)) + " expected output: True "
print str(make_bricks(1000000, 1000, 1000100)) + " expected output: True"
print str(make_bricks(2, 1000000, 100003)) + " expected output: False"
print str(make_bricks(20, 0, 19)) + " expected output True "
print str(make_bricks(20, 0, 21)) + " expected output False"
print str(make_bricks(20, 4, 51)) + " expected output False"
print str(make_bricks(20, 4, 39)) + " expected output True "