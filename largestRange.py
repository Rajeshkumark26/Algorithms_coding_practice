'''
i/p :[1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
o/p :[0,7]

'''





def largestRange(array):
   	
	values = {} 
	wLength=0
	bestRange=[]
	for num in array:
		values[num]=True
		
	for num in array:
		if not values[num]:
			continue
		values[num]	= False
		left = num-1
		right= num+1
		cLength=1
		while left in values:
			values[left]=False
			cLength += 1 
			left -= 1
		while right in values:
			values[right] = False
			cLength += 1
			right += 1
		if cLength > wLength:
			wLength=cLength
			bestRange=[left+1,right-1]
	return bestRange