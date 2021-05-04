"""
i/p : [2, 1, 5, 2, 3, 3, 4]
o/p : 2
"""


def firstDuplicateValue(array):
    seen=set()
	for value in array:
		if value in seen:
			return value
		seen.add(value)
    return -1