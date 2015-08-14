
#Question:
#With a given integral number n, write a program to generate a dictionary that contains
#(i, i*i) such that is an integral number between 1 and n (both included).
#and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}



def main():
        x=print(input("Enter" ))
        fval = fact(x)
        print("x! is {}".format(fval))

def fact(val):
    f=1
    if val>=2:
        while(val>=2):
            x,y=val,val-1;
            val=val-2
            f=f*x*y
        return f
    elif val < 0:
        return "Input should be positive"
    elif val == 0:
        return 1
    else: return val;


if __name__=="__main__":main()
