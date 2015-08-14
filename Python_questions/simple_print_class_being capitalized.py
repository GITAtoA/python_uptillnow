class A():
    def __init__(self):
        self.lisst=[]
        self.strinng=""
    def g(self):
    	while(True):
    		self.strinng=str(input("Enter : "))
    		self.lisst.append(self.strinng.upper())
    		self.p=int(input("(1/0)? "))
    		if (self.p)==0:
    			break
    def sc(self):
        print(self.lisst)

t=A()
t.g()
t.sc()
