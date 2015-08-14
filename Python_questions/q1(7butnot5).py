l=[];
for _ in range(2000,3201):
	if(_%7==0 and _%5!=0):
		l.append(str(_))
print(",".join(l))
