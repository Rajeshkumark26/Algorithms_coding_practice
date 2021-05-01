"""
string = 'xyz'
key=2
output='zab'
"""

def caesarCipherEncryptor(string, key):
    newString=[]
	
	for letter in string:
		key = key % 26
		newKey = ord(letter) + key
		newString.append(chr(newKey)if newKey <=122 else chr(96 + newKey % 122))
	return ''.join(newString)	