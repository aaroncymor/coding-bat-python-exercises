def make_bricks(small, big, goal):
	if goal % 5 > 0:
		temp = goal % 5
		if temp <= small:
			if ((goal - temp) / 5) <= big:
				return True
	else:
		temp = goal % 5
		if temp <= big:
			return True
		elif goal <= small:
			return True
	return False

