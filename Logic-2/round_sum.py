def round_sum(a,b,c):
	addend = []
	addend.append(a)
	addend.append(b)
	addend.append(c)
	
	total = 0
	for i in range(len(addend)):
		total += round_number(addend[i])
	
	return total
	
def round_number(num):
	str_num = str(num)
	last_digit = int(str_num[len(str_num) - 1])
	if last_digit >= 0 and last_digit < 5:
		return (num - last_digit)
	elif last_digit >=5 and last_digit < 10:
		return (num + (10 - last_digit))
		
		
print round_sum(16,17,18)
print round_sum(12,13,14)
print round_sum(6,4,4)
print round_sum(0,0,1)