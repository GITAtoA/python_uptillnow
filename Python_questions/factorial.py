

def main():
        x=int(input("Enter the value: "))
        fval=fact(x)
        print("x! is {}".format(fval))



def fact(val):
    f=1
    if(val>=2):
        while(val>=2):
            x,y=val,val-1;
            val=val-2
            f=f*x*y
        return f
    elif val<0:
        return "Input should be positive"
    elif val == 0:
        return 1
    else: return val;


if __name__=="__main__":main()
