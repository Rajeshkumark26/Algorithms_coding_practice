"""
i/p : ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
o/p : [
  ["foo"],
  ["flop", "olfp"],
  ["oy", "yo"],
  ["act", "cat", "tac"]
]

"""



def groupAnagrams(words):
	anagrams={}
	
    for word in words:
		sortedWord=''.join(sorted(word))
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
			anagrams[sortedWord]=[word]
	return list(anagrams.values())