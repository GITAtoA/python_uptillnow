
print("Functions Cheat sheet")
def fn():
    print("Checking Functions")
    
def fn_arg(age):
    age_limit=age//2+7
    return age_limit

dating_girl_age_limit=fn_arg(23)
print("So the age i can date is",dating_girl_age_limit,"and above")

    
print("Default value for arguments")

def get_gender(sex='unknown'):
    if sex is'm':
        print("Males")
    elif sex is'f':
        print("female")
    else:
        print("unknown")

get_gender('m')
get_gender('f')
get_gender()

def literature(name='Abhinav',action='is',item='Awesome'):
    print(name,action,item)

literature()
literature('Abhinav', 'is', 'hardworker')
literature(name='Varun',item='cool')

print("Awesome now lets build a calculator")
print("Addition of 1+2+3+4+5")

def addition(*args):
    total=0
    for n in args:
        print("adding",total,"to",n)
        total += n
    print("total is",total )

addition(1,2,3,4,5)

def subtraction(*args):
    total=5000
    for n in args:
        print(total,"subtracted by",n)
        total -= n
    print("total is",total)

subtraction(2000,1000,500,250,250)

def multiplication(*args):
    total=1
    for n in args:
        print(total,"multiplied",n)
        total *= n
    print("total is",total)

multiplication(2,2,2,2,2)


def division(*args):
    total=1024
    for n in args:
        print(total,"divided by",n)
        total //= n
    print("total is",total)

division(2,2,2,2,2)

print("Getting all argument in a list once for all using *list_name")
def health_cal(age=1,apples=1,ciggerets=0):
    health_value=(age*100)+(apples*5)-(ciggerets*10)
    print(health_value)
data_list=[23,3,0]
health_cal(data_list[0],data_list[1], data_list[2])
health_cal(*data_list)
