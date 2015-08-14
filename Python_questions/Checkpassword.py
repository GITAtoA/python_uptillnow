import re

li=[]
def main():
    
    print('''\
    Following are the criteria for the password:
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    ''')
    password = input("Enter your password and we will tell which one is valid : \n")
    pass_split =password.split(',')
    print(pass_split)
    check_passwords(pass_split)
    print("Acceptable Strings are  : ")
    print(",".join(li))
    
def check_passwords(splitted_list):
    for _ in splitted_list:
        if not re.search("[a-z]",_):
            print("{}  must have at-least one Lower case alphabets\n".format(_))
            continue
        if not re.search("[A-Z]", _):
            print("{} must have at-least 1 UPPERCASE alphabet\n".format(_))
            continue
        if not re.search("[0-9]", _):
            print("{} Must have at-least 1 UPPERCASE alphabet\n".format(_))
            continue
        if not re.search("[#$@]",_):
            print("{} Must contain at-least one of $ or # or @\n".format(_))
            continue
        if len(_)<6:
            print("{} Must have length > 6\n".format(_))
            continue
        if len(_)>12:
            print("{} Must have length <12\n".format(_))
            continue
        li.append(_)
        
        
                      
if __name__=="__main__":main()