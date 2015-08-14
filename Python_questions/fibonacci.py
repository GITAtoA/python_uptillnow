

a,b = 0,1
print ("Fibonacci Series")
for _ in range(20):
     a,b = b, a+b
     print("{}".format(b),end = ' ')
