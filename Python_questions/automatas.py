def getString(currentStr, aCount, bCount, maxLength):
	if maxLength == 0:
		if (aCount-bCount)%3>0:
			print(currentStr, "\t\t || #a: ", aCount,
			                         " #b: ", bCount,
			                         " #(a-b): ", aCount-bCount,
			                         " #(a-b)mod 3: ", (aCount-bCount)%3)
		return
	getString(currentStr + 'a', aCount+1, bCount, maxLength-1)
	getString(currentStr + 'b', aCount, bCount+1, maxLength-1)
 
def LanguageTwo(maxLength):
	for i in range(1,maxLength+1):
		getString('', 0, 0, i)
 
'''
Usage: Call the function LanguageTwo() with the desired maximum length.
Example:
LanguageTwo(5) will print all strings of length<=5 which belong in the lanague two,
L = {w: no of a's - no of b's)mod 3 >0}
'''
 
LanguageTwo(3)