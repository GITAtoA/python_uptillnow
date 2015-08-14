
#Defining a new class to test inheritance and multiple inheritance

def main():
    b = to_check_classes()
    b.smallVillage_weeklyincome()
    b.bigVillage_to_smallCit()
    b.smallCity_to_big_city()

class to_establish_small_village:
    def __init__(self):
        print("Money(minimum) to establish a Village : $ 70K  \nBasic need is 1000MW of Energy/week and 5000liters of Water/day")
        starting_money = int(input("Enter your budget in $"))
        while True:
            if starting_money >=70000:
                print("You can start your own village")
                break 
            else:
                print("You don't have the minimum requirements.Come Back again!")
                starting_money = int(input("Enter your budget in $"))
    
    def smallVillage_weeklyincome(self):
        print("You get you small village see you in a month \n")
        weekly_income=int(input("What is weekly income of your Village in $"))
    
        while weekly_income:
            if(weekly_income <35000):
                print("You need more income.Come Back when you have it.See you in a month!!")
                weekly_income=int(input("Enter your weekly income of Village in $"))
            else:
                print("You have the basic need for small village to big village.See you in a month!!")
                break

class smallvillage_to_bigvillage():
    def bigVillage_to_smallCit(self):
        print("You get you big village see you in a month \n")
        weekly_income=int(input("What is weekly income of your Village in $"))
    
        while weekly_income:
            if(weekly_income <105000):
                print("You need more income.Come Back when you have it.See you in a month!!")
                weekly_income=int(input("Enter your weekly income of Village in $"))
        
            else:
                print("You have the basic need for  big village to small city.See you in 6 month!!")
                break

class big_village_to_smallcity():
    def smallCity_to_big_city(self):
        print("You get you small City see you in  a year \n")
        weekly_income=int(input("What is weekly income of your city in $"))
    
        while weekly_income:
            if(weekly_income <2000000):
                print("You need more income.Come Back when you have it.See you in a month!!")
                weekly_income=int(input("Enter your weekly income of City in $"))
        
            else:
                print("You have the basic need for  big City to small city.See you in a year!!")
                break
        
    
class to_check_classes(to_establish_small_village,smallvillage_to_bigvillage,big_village_to_smallcity):#inheriting All classes
    pass

if __name__ == '__main__':main()


        
#########################################################################################################################################################################################################################################
'''class male:
    
    
    class_variable_gender ="male"#"default value for class_variable this can be altered any time"
    
    class_varuable2_age = 23 #lets use this as integer
    
    
    def __init__(self,argu_name): #self.something has the scope of object
        
        self.instance_name=argu_name

    def get_name(self):
    
        print(self.instance_name)



ob = male("Abhinav123")  #sending argu_name as Abhinav123 as default value used as constructor or for initializing

ob.get_name()   #calling function

print("default value was",ob.class_variable_gender)

ob.class_variable_gender = 'female' # as we can see it can be altered

print("now its changed to after alteration",ob.class_variable_gender) #result of alteration is here

print("default value of class_variable_name is ",ob.class_varuable2_age) 

ob.class_varuable2_age=34 #similarly

print("Altered value of class_variable_name is now",ob.class_varuable2_age) '''

####################################################################################################################
