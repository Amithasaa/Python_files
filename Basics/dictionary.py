<<<<<<< HEAD
'''
Dictionaries are mutable.
'''

d1 = {'name': 'Amitha','age':27,'phone':23456}
print(d1,type(d1)) #{'name': 'Amitha', 'age': 27, 'phone': 23456} <class 'dict'>

#In dict we cannot store duplicate keys
d1['name'] = 'Pooja'
print(d1) #{'name': 'Pooja', 'age': 27, 'phone': 23456}

d1 = {'name': 'Amitha','age':27,'phone':23456,'age':29}
print(d1) #{'name': 'Amitha', 'age': 29, 'phone': 23456}

#In dict we can store duplicate values.
marks = {'sci':45,'math':45}
print(marks) #{'sci': 45, 'math': 45}

for i in d1.keys():#name age phone
    print(i)
    
for i in d1.values(): # Amitha 29 23456
    print(i)

for i in d1.items(): 
    print(i)
#('name', 'Amitha')
#('age', 29)
#('phone', 23456)
=======
'''
Dictionaries are mutable.
'''

d1 = {'name': 'Amitha','age':27,'phone':23456}
print(d1,type(d1)) #{'name': 'Amitha', 'age': 27, 'phone': 23456} <class 'dict'>

#In dict we cannot store duplicate keys
d1['name'] = 'Pooja'
print(d1) #{'name': 'Pooja', 'age': 27, 'phone': 23456}

d1 = {'name': 'Amitha','age':27,'phone':23456,'age':29}
print(d1) #{'name': 'Amitha', 'age': 29, 'phone': 23456}

#In dict we can store duplicate values.
marks = {'sci':45,'math':45}
print(marks) #{'sci': 45, 'math': 45}

for i in d1.keys():#name age phone
    print(i)
    
for i in d1.values(): # Amitha 29 23456
    print(i)

for i in d1.items(): 
    print(i)
#('name', 'Amitha')
#('age', 29)
#('phone', 23456)
>>>>>>> 6729aa240a7a25022ef447f4c282c6c15ddfe66b
