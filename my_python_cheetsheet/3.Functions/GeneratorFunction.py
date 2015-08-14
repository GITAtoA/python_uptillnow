def putNumbers(n):
	    i = 0
	    print('k')
	    while i<n:
	        j=i
	        print("Check for",j)
	        i=i+1
	        if j%7==0:yield j
for i in putNumbers(100): # i is what putnumber will return and that will be printed
	print("In main printing : {}".format(i))