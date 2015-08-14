dictionary = {'key1':' has Value1','key2':' has value2','key3':' has value3'}
#dictionary has two part keys and values

for k,v in dictionary.items():
    print(k,v)
print(" initial dictionary",dictionary)

dictionary['key10']= 'has value10' #Creating key by assingment

for k,v in dictionary.items():
    print(k,v)
print("adding a value  key10 : 'has value10'",dictionary)

dictionary["key5"]='have value5'
print(dictionary['key5'])


del dictionary['key5']
print(dictionary)
