#decval= int(input("Enter a binary value : "))
#print("{0:i}".format(decval))
#TO enter a bunch of binary values and print the values divisible by 5

x=10
op=1
l=[]
print("Binary value of 10 is {0:b}\nEnter value similar to {0:b}".format(x,x))
while(op):
	binvalue=str(int(input("\nEnter a binary value : ")))
	y=(int(str(binvalue),2))
	l.append(y)
	op=int(input("\nWant to enter more ?(0/1)....."))
print(l)

for _ in l:
	if _%5==0:
		print("\nValue  is {} and is divisible by 5 :) ".format(_))
	#(remove to see effects)else :
	#(remove to see effects)	print("\nValue is {} and is NOT divisible by 5".format(_))