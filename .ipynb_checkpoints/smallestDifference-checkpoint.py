"""
input : arrayOne : [-1, 5, 10, 20, 28, 3]
        arrayTwo : [26, 134, 135, 15, 17]
        output   : [28, 26]
"""



def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	arrayOne.sort()
	arrayTwo.sort()
	oneIdx=0
	twoIdx=0
	smallest = float('inf')
	current = float('inf')
	while oneIdx < len(arrayOne) and twoIdx < len(arrayTwo):
		firstNum = arrayOne[oneIdx]
		secondNum = arrayTwo[twoIdx]
		if firstNum < secondNum :
			current = secondNum - firstNum
			oneIdx += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			twoIdx += 1
		else:
			return [firstNum,secondNum]
		if smallest > current:
			smallest = current
			smallestpair=[firstNum,secondNum]
	return smallestpair