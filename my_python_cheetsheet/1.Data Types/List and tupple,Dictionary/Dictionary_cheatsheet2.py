__author__ = 'Abhinav'

dic={'lname':'Rana','fname':'Abhinav','job':'jobless'}
dic2={'a':200,'b': 30,'c':  40}

kvalues=dic.keys()
vvalues=dic.values()
print(kvalues)
print(vvalues)


print(sorted(dic2.values()))
print(min(dic2.values()))
print(max(dic2.values()))

for keys in sorted(dic):
    print(keys,"=>",dic[keys])

for keyss in sorted(dic2):
    print(keyss,"=>",dic2[keyss])

