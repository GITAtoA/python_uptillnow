__author__ = 'Abhinav'
import random

# list unpacking and arguments


def ice_cream(flavor,topping='cherry',type='normal'):
    print("You ordered flavor as : ",flavor)
    print("With, topping : ",topping)
    print("and your ice cream is : ",type)

flavor=['Vanilla','Chocolate','Butterscotch','Tootyfruitty']
topping=['cherry','chocolate sauce','choco chips','fruit dip']
type=['thick','extra thick']
ice_cream(random.choice(flavor))
ice_cream(random.choice(flavor),random.choice(topping),random.choice(type))


print(int(random.random()*10))
print(int(random.randint(0,5)))

## unpacking

lisst=[2,10]
print(*lisst)

a = range(3,10)
print(*a)
b=dict( a=10,b=20,c=30)

