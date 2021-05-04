"""
i/p : [
  [1, 2],
  [3, 5],
  [4, 7],
  [6, 8],
  [9, 10]
]

o/p : [
  [1, 2],
  [3, 8],
  [9, 10]
]

"""


def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals,key=lambda x:x[0])
    mergedIntervals=[]
    currentInterval=sortedIntervals[0]
    mergedIntervals.append(currentInterval)
    for nextInterval in sortedIntervals:
        print(nextInterval)
        _, currentIntervalEnd= currentInterval
        nextIntervalStart,nextIntervalEnd=nextInterval
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1]=max(currentIntervalEnd,nextIntervalEnd)
            print('current interval',currentInterval)
        else:
            print('this is appending',nextInterval,mergedIntervals)
            currentInterval=nextInterval
            mergedIntervals.append(currentInterval)
            print('after merging',mergedIntervals)
    return mergedIntervals