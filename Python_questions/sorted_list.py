l=[]
while(True):
	i = str(input("Enter data : "))
	o = int(input("Want to enter more(1/0) ?"))
	if(o==0):break;
	l.append(i)
print(l)
print(sorted(l))