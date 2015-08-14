i=int(input("ROW : "))
j=int(input("COLUMN : "))
multilist=[[0 for x in range(j)]for y in range(i)]
for r in range(i):
	for c in range(j):
		multilist[r][c]=r*c

print(multilist)
