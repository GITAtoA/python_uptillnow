

'''
Question:
	Write a program that computes the net amount of a bank account 
	based a transaction log from console input. The transaction log 
	format is shown as following:
	D 100
	W 200
	¡¬
	D means deposit while W means withdrawal.
	Suppose the following input is supplied to the program:
	D 300
	D 300
	W 200
	D 100
	Then, the output should be:
	500

'''

def main():
    sum = transaction()
    print("After transaction sum is {}".format(sum))
    
def transaction():
    val = 1 
    sum =0
    while(val):
        s=input("D for Draw\bW for withdraw\nFollowed by space and Value") 
        words = s.split(" ")       
        if words[0] == 'W':
            sum -=int(words[1])
        elif words[0] == 'D':
            sum +=int(words[1])
        val = int(input("\n Want to enter another Transaction ? (0/1) : "))
    print("Transaction happening........\n")
    return sum
   

    

if __name__=="__main__":main()
