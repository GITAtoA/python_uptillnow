#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#List :['34', '67', '55', '33', '12', '98']
#Tuple:('34', '67', '55', '33', '12', '98')
lis=[]
for i in range(5):
	val=(input("Enter: "))
	lis.append(val)
print(lis)
t=tuple(lis)
print(t)