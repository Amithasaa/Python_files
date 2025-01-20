<<<<<<< HEAD
'''
In set we can store homogeneous as wll as heterogeneous data
Set is an unordered collection of data means set does not support indexing
Set does not support indexing of data
In set we cannot store duplicates.
Sets are mutable.
'''

s1 = {10,True,'Kodnest', 10, 20,55.44}
print(s1, type(s1)) #{True, 'Kodnest', 20, 55.44, 10} <class 'set'>
#print(s1[0]) // error

#add():Add an element in the set.
s1.add(500)
print(s1) #{True, 20, 500, 55.44, 10, 'Kodnest'}

#remove(): Removes an element in the list
s1.remove(55.44)
print(s1) #{True, 20, 500, 'Kodnest', 10}

#pop() :Without index It will remove random element in the set and return one element
poped_ele = s1.pop()
print(poped_ele) #Kodnest
print(s1) # {'Kodnest', 20, 500, 10}

#del: It deletes The complete set
=======
'''
In set we can store homogeneous as wll as heterogeneous data
Set is an unordered collection of data means set does not support indexing
Set does not support indexing of data
In set we cannot store duplicates.
Sets are mutable.
'''

s1 = {10,True,'Kodnest', 10, 20,55.44}
print(s1, type(s1)) #{True, 'Kodnest', 20, 55.44, 10} <class 'set'>
#print(s1[0]) // error

#add():Add an element in the set.
s1.add(500)
print(s1) #{True, 20, 500, 55.44, 10, 'Kodnest'}

#remove(): Removes an element in the list
s1.remove(55.44)
print(s1) #{True, 20, 500, 'Kodnest', 10}

#pop() :Without index It will remove random element in the set and return one element
poped_ele = s1.pop()
print(poped_ele) #Kodnest
print(s1) # {'Kodnest', 20, 500, 10}

#del: It deletes The complete set
>>>>>>> 6729aa240a7a25022ef447f4c282c6c15ddfe66b
del s1