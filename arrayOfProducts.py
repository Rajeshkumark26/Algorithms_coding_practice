"""
i/p : [5, 1, 4, 2]
o/p : [8, 40, 10, 20]

note : without using division operator
"""


def arrayOfProducts(array):
	leftProduct=1
	rightProduct=1
	products=[1 for _ in range(len(array))]
	for i in range(len(array)):
		products[i] = leftProduct
		leftProduct *= array[i]
	for i in reversed(range(len(array))):
		products[i] *= rightProduct
		rightProduct *= array[i]
	
	return products