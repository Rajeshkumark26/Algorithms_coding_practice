'''
i/p : "1921680"
o/p : ["1.9.216.80", "1.92.16.80", "1.92.168.0", "19.2.16.80", "19.2.168.0", "19.21.6.80", "19.21.68.0", "19.216.8.0", "192.1.6.80", "192.1.68.0", "192.16.8.0"]

'''





def validIPAddresses(string):
    ipAddress=[]
	for i in range(1,min(len(string),4)):
		currIP=['','','','']
    	currIP[0]=string[:i]
		if not isValidPart(currIP[0]):
			continue
		for j in range(i+1,i+min(len(string)-i,4)):
			currIP[1]=string[i:j]
			if not isValidPart(currIP[1]):
				continue
				
			for k in range(j+1,j+min(len(string)-j,4)):
				currIP[2]=string[j:k]
				currIP[3]=string[k:]
				if isValidPart(currIP[2]) and isValidPart(currIP[3]):
					ipAddress.append(".".join(currIP))
	return ipAddress

def isValidPart(string):
	stringAsInt = int(string)
	if stringAsInt > 255:
		return False
	return len(string) == len(str(stringAsInt))
		