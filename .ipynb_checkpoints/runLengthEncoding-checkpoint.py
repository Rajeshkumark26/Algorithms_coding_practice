"""
input : "AAAAAAAAAAAAABBCCCCDD"
output: "9A4A2B4C2D"
"""


def runLengthEncoding(string):
    runLength=1
	encodedString=[]
	for i in range(1,len(string)):
		currString=string[i]
		prevString=string[i-1]
		if currString != prevString or runLength==9:
			encodedString.append(str(runLength))
			encodedString.append(prevString)
			runLength=0
		runLength += 1
	#last run
	encodedString.append(str(runLength))
	encodedString.append(string[-1])
	return ''.join(encodedString)