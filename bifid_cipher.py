import timeit
from timeit import default_timer as timer

table = (('J', 'D', 'I', 'E', 'C'),
		 ('H', 'Ä', 'A', 'U', 'R'),
		 ('V', 'B', 'S', 'K', 'L'),
		 ('T', 'O', 'M', 'G', 'P'),
		 ('F', 'Ö', 'N', 'Å', 'Y'))
		 
def executionTime(function):
	def wrapper(*args):
		start = timer()
		ret = function(*args)
		end = timer()
		print("%.5f ms" % ((end-start) * 1000))
		return ret
	return wrapper

@executionTime		 
def bifidEncrypt(word):
	yCoordinates = []
	xCoordinates = []
	digitsList = []
	
	for char in word:
		for rowIndex in range(len(table)):
			if char in table[rowIndex]:
				yCoordinates.append(rowIndex)
				xCoordinates.append(table[rowIndex].index(char))
				break
				
	digitsList = yCoordinates + xCoordinates

	encryptedWord = ""

	for index in range(0, len(digitsList), 2):
		encryptedWord += table[digitsList[index]][digitsList[index + 1]]
		
	return encryptedWord

@executionTime
def bifidDecrypt(word):
	digitsList = []
	
	for char in word:
		for rowIndex in range(len(table)):
			if char in table[rowIndex]:
				digitsList.append(rowIndex)
				digitsList.append(table[rowIndex].index(char))
				break
				
	decryptedWord = ""
	
	for index in range(len(digitsList) // 2):
		decryptedWord += table[digitsList[index]][digitsList[index + len(digitsList) // 2]]
		
	return decryptedWord