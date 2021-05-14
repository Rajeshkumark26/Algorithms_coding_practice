'''
i/p : "AlgoExpert is the best!"
o/p : "best! the is AlgoExpert"

'''




def reverseWordsInString(string):
    # Write your code here.
	words=[]
	sow=0
	for idx in range(len(string)):
		character = string[idx]
		if character == ' ':
			words.append(string[sow:idx])
			sow=idx
		elif string[sow]==' ':
			words.append(' ')
			sow=idx
	words.append(string[sow:])		
	start=0
	end=len(words)-1
	while start < end:
		words[start],words[end]=words[end],words[start]
		start += 1
		end -= 1
		
    return ''.join(words)