<<<<<<< HEAD
'''
In list we can store homogeneous as well as heterogeneous data.
In list we can store duplicate values.
List is an ordered collection of data: Order of insertion will remain as it is in the output.
Lists are mutable: Once we declare the list we can modify it.

'''

lis = [10,20,30,40,True,'Kodnest',20]
print(lis, type(lis))

#Append method will add element at the end of the list
lis.append(30)
print(lis)

#insert(index,element): inserts element at specified index.
lis.insert(1,15)
print(lis)

#remove(element) : Removes first occurence of the specified element.
lis.remove(20)
print(lis)


#Accessing list elements
print(lis[0])

#in and not in Operators:
print(2000 in lis)
print('Kodnest' in lis)

#pop : Without argument will delete  and return last element from the list
removed_ele = lis.pop()
print(removed_ele)
lis.pop()
print(lis)

#pop(index): With argument will delete the ele at specified index
removed_ele = lis.pop(4)
print(removed_ele) #kodnest
print(lis)

#del keyword:del won't return item but pop will return an item
del lis[1]
print(lis)

del lis
=======
'''
In list we can store homogeneous as well as heterogeneous data.
In list we can store duplicate values.
List is an ordered collection of data: Order of insertion will remain as it is in the output.
Lists are mutable: Once we declare the list we can modify it.

'''

lis = [10,20,30,40,True,'Kodnest',20]
print(lis, type(lis))

#Append method will add element at the end of the list
lis.append(30)
print(lis)

#insert(index,element): inserts element at specified index.
lis.insert(1,15)
print(lis)

#remove(element) : Removes first occurence of the specified element.
lis.remove(20)
print(lis)


#Accessing list elements
print(lis[0])

#in and not in Operators:
print(2000 in lis)
print('Kodnest' in lis)

#pop : Without argument will delete  and return last element from the list
removed_ele = lis.pop()
print(removed_ele)
lis.pop()
print(lis)

#pop(index): With argument will delete the ele at specified index
removed_ele = lis.pop(4)
print(removed_ele) #kodnest
print(lis)

#del keyword:del won't return item but pop will return an item
del lis[1]
print(lis)

del lis
>>>>>>> 6729aa240a7a25022ef447f4c282c6c15ddfe66b
print(lis) #Error: Name lis is not defined