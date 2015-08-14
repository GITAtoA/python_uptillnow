#Write a program, which will find all such numbers between 1000 and 3000
#(both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence 
#on a single line.
l=[]
count=0
x=int(input("Enter starting point:  "))
y=int(input("Enter End point:  "))
for _ in range(x,y+1):
	stg = str(_)# 2,0,0,0
	count=0
	for x in stg:
			if int(x)%2==0:
		 		count+=1
	if count==len(stg):
		l.append(_)
print(l)