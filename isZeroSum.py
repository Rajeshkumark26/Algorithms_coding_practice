array=[-3,4,-3,-1,1]

def isZeroSum(array):
    preSum=0
    h=set()
    for i in range(len(array)):
        preSum += array[i]
        if preSum == 0 or preSum in h:
            return True
        else:
            h.add(preSum)
    return False        

isZeroSum(array)