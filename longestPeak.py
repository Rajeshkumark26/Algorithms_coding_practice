"""
i/p : [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
o/p : 6

"""



def longestPeak(array):
	longestPeak=0
	i=1
	while i < len(array) -1 :
		isPeak = array[i] > array[i-1] and array[i] > array[i+1] 
		if not(isPeak):
			i += 1
			continue
			
		leftIdx = i-2
		rightIdx = i+2
		while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
			leftIdx -= 1
		while rightIdx < len(array)	and array[rightIdx] < array[rightIdx -1]:
			rightIdx += 1
		currentLongest = rightIdx - leftIdx -1
		longestPeak = max(longestPeak,currentLongest)
		i=rightIdx
	return longestPeak