'''
Use of List and Tuples ,also
List is more like pencil and tupple is  more like a pen
In list values can be changed anytime and in tupple it cannot be done once it is
made it is done no further can you change the value you can clear and delete it
using del and clear() functions
del
.clear()
.append(x) x as value
.reverse()
.insert() or s[i:i] = t
replacement of items s[i:j:k]='t' iterable also exactly the same to be replaced

'''


list1=[10,20,30,40,50,'Apple']
list2 =[100,200,300,"HELLO"]
a,b,c =0,1,2

print("Testing Lists or pencils")
list1.append(300) #append value permanently

print(list1) # to print list

list1[6:] = ['Oranges','Banana']     #from 6 onwards keep adding what values given permanently
print(list1 +['Ab'])                #temporary adding of value using '+' operator
print(list1)

list1=list2 #copy and change values of list1 by list2
list3 =list1.copy()
print("list3 =list1.copy()",list3)
print("this will input all values from list 2 to list 1 : \n",list1)

list1 = [] #clear list :) or
# or list1.clear()
print("list1 = [] ",list1)


#del list deletes the list i.e from the memory
'''
del list1
print("This will never be printed",list1) # this line would show error
'''


list2 =['hi',1,2,True] # recreate list 2
print("list2 is  : ",list2 )
print("list2[1:3] is ",list2[1:3]) # [1:(this value -1)]

list2.clear()
print("This list2.clear would clear the list2",list2)

'''del list2
print("deletes the list2 from the memory")
print(list2) # this will never be shown and will input error so is in comments
'''


lisst =[10,20,30,40,50,60,70,80,90,100]
print(lisst)
lisst[1:4] = [2,3,4,5,6,7] #replaces all the values in 1 to 3  by values given in case here [2,3,4,5,6,7]
print(lisst)
print(lisst[3::2])
lisst[3::2]=['this','is',list2,3,4] #when using list[i,j,k] i.e replacement should be equal to  no of items when list[i,j,k]
print(lisst)  # 5 items will be displayed with lisst[3::2] so  replace it with 5 items i.e  ['this','is',list2,3,4]

lisst.insert(0,'ABhinav') # same as list[i:i]=[45]
lisst[2:2]=[45]
print("lisst.insert('ABhinav',0) and lisst[2:2] : ",lisst) #permanent Insert
print(lisst)



print("Testing tuples or Pens")

tup1=(2,3,4)
print('tup1',tup1)

tup=(1,2,3,4,5,'six','seven',True,tup1)
print("tup :",tup)

tup1=tup            #tuples can be copied to other tuples
print('tup1',tup1)

'''
tup[2:5]=()         #cannot change it any further
print("tup[2:5] =(45,47,48) : ", tup)'''



#del tup
#print("tuple is : ",tup) # this will show error
del lisst
del list2
del list1
del tup1
del tup
print('In built function list()',list(range(5,100,5)))