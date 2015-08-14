
  # references to the object 20, 20 is an object with its own type and id
a = 20    
print(id(a),type(a),a)

b = 20
print(id(b),type(b),b)

print('a==b : ',a==b)
print('a is b : ',a is b)

c = 21

print(id(c),type(c),c)
print('a==c : ',a==c)
print('a is c : ',a is c)

print('\nNow lets take some list and test for references')
list1=[10,20,30,40]
print('list1 : ',list1)
print(id(list1),type(list1))

list2=list1
print('list2 : ',list2)
print(id(list2),type(list2))

print('We see that both list1,list2 var name references to the same list')
print('Now lets change the value of the first element in the list')

list1[0]=30
print('\nlist1[0]=30')
print('Now list1 is',list1,'and list2 is',list2)
print('As we can see as both the names points or references to the same object \n')


d= dict(x=10,y=20)
di=dict(x=10,y=20)
print("dictionary1",d,"dictionary2",di)
print('id(d)',id(d),'type(d)',type(d))
print('id(di)',id(di),'type(di)',type(di))
print('d==di',d == di)
print('d is di',d is di)