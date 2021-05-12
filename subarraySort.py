'''
i/p:[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
o/p:[3, 9]
'''





def subarraySort(array):
	minimum=float("inf")
	maximum=float("-inf")
	out=0
	
	def outOrder(i,array):
		if i==0:
			return array[i+1] < array[i]
		if i==len(array)-1:
			return array[i-1]>array[i]
		return array[i+1] < array[i] or array[i-1]>array[i]
		
	for i in range(len(array)):
		if (outOrder(i,array)):
			minimum=min(minimum,array[i])
			maximum=max(maximum,array[i])
	if minimum==float('inf'):
		return [-1,-1]
	leftIdx=0
	rightIdx=len(array)-1
	
	while minimum >= array[leftIdx]:
		leftIdx += 1
	while maximum <= array[rightIdx]	:
		rightIdx -= 1
		
	return [leftIdx,rightIdx]	
		