"""
i/p : "abcdcaf"
o/p :  1


"""



def firstNonRepeatingCharacter(string):
    characters={}
	for char in string:
		if char not in characters:
			characters[char]=0
		characters[char] += 1
	for idx,char in enumerate(string):
		if characters[char]==1:
			return idx
    return -1