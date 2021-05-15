'''
i/p : [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]

o/p : [-24, 2, 3, 5, 6, 35]

'''



def longestIncreasingSubsequence(array):
    seq=[None for x in array]
	leng=[1 for x in array]
	maxlen=0
	for i in range(len(array)):
		curr=array[i]
		for j in range(0,i):
			other=array[j]
			if other < curr and leng[j]+1 > leng[i]:
				leng[i]=leng[j]+1
				seq[i]=j
		if leng[i]>=leng[maxlen]	:
			maxlen=i
	return build(array,seq,maxlen)			

def build(array,seq,currIdx):
	sequence=[]
	while currIdx is not None:
		sequence.append(array[currIdx])
		currIdx=seq[currIdx]
	return list(reversed(sequence))	