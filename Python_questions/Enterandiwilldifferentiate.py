#From a string calculate number of Letters and Numbers

input_str=(input("Enter and i will differentitate"))
numvales= dict(LETTERS=0,WORDS=0,OTHERS=0)
#print(numvales)
for c in input_str : 
	if(c.isalpha()):
		numvales['WORDS']+=1
	elif(c.isdigit()):
		numvales['LETTERS']+=1
	else:
		numvales['OTHERS']+=1

print(input_str)
for k in numvales:
	print(k,numvales[k],end=" ")