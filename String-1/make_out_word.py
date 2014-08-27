"""
	Given an "out" string length 4, such sa "<<>>", and a word, return a new string where the word is
	is the middle of the out string, e.g. "<<word>>"
"""

def make_out_word(out,word):
	new_formed_str = ''
	if len(out) % 2 == 0:
		i = 0
		j = len(out) / 2
		while i <= 1:
			new_formed_str += out[i]
			i += 1
		
		new_formed_str += word
		
		while j <= (len(out)/2) + 1:
			new_formed_str += out[j]
			j += 1
			
	return new_formed_str
