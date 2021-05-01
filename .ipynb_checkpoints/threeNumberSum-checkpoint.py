"""
array : [12, 3, 1, 2, -6, 5, -8, 6]
target sum= 0
o/p : [
  [-8, 2, 6],
  [-8, 3, 5],
  [-6, 1, 5]
]
"""


def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	triplets=[]
	for i in range(len(array)-2):
		left= i + 1
		right= len(array) - 1
		while left < right :
			currSum=array[i] + array[left] + array[right]
			if currSum==targetSum:
				triplets.append([array[i],array[left],array[right]])	
				right -= 1
				left += 1
			elif currSum > targetSum:
				right -= 1
			elif currSum < targetSum: 
				left += 1
	return triplets