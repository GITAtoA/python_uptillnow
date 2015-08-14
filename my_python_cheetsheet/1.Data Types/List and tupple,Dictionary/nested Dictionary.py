__author__ = 'Abhinav'

d = {'name':{'fname':'Abhinav','lname':'Rana'},'job':['jobless'],'age':23.6}
print("the dictionary is :",d)

print(d['name']['fname'])
d['fathersname']={'fname':'Atul'}
d['fathersname']={'mname':'Kumar'}
d['fathersname']={'lname':'Rana'}

d['motherssname']={'fname':''}
d['motherssname']={'lname':''}

d['motherssname']['fname'] ='Seema'

d['motherssname']['lname'] ='Rana'

print(d['motherssname']['lname'][-2])
d['job'].append('coder')

print(d)
