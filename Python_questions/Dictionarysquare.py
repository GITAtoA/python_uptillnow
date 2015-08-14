#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
print("Give us a limit and we will make a dictionary of squares with that limit")
val = int(input("Enter the limit: "))
d=dict()
for k in range(val+1):
	d[k]=k*k
print(d)
