'''
Write a program that accepts a sequence of whitespace separated
 words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
OR sorted list of set
'''
l=[]
while(True):
    strr=str(input("Enter : "))    
    l.append(strr)
    p=int(input("(1/0)? "))
    if(p==0):break
t=sorted(set(l))
print(t)

''' OUTPUT
Enter : zzz
(1/0)? 1
Enter : zzz
(1/0)? 1
Enter : zzz
(1/0)? 1
Enter : yyy
(1/0)? 1
Enter : yyy
(1/0)? 1
Enter : yyy
(1/0)? 1
Enter : bbbbbb
(1/0)? 1
Enter : bbbbbb
(1/0)? 1
Enter : aaaa
(1/0)? 1
Enter : aaaa
(1/0)? 0
['aaaa', 'bbbbbb', 'yyy', 'zzz']
'''