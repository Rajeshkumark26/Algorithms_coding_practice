'''
i/p:[8, 4, 2, 1, 3, 6, 7, 9, 5]
o/p:25
'''



def minRewards(scores):
    rew=[1 for _ in range(len(scores))]
	
	for i in range(1,len(scores)):
		if scores[i] > scores[i-1]:
			rew[i]=rew[i-1]+1
			
	for i in reversed(range(len(scores)-1)):
		if scores[i] > scores[i+1]:
			rew[i] = max(rew[i],rew[i+1]+1)
	return sum(rew)		