'''
In tuple wecam store homogeneous as well as heterogeneous data
In tuples we can store duplicates
Tuples are ordered collection of data
Tuples are immutable: Once we declare the tuple we cannot modify it.

'''

tup1 = (10,20.55,'kodnest',True,10)
print(tup1 ,type(tup1))
#tup1.remove(55)
#del.pop()
#del tup1[2]

#deletes the complete tup1 object
del tup1
# print(tup1[2])

#Concatenating
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3)

#Interview question
#Create singleton Tuple: Declare a tuple with 1 element give the comma is the logic
tup = (10,)
print(tup, type(tup))

#unpacking
new_tuple = (10,20,30,40)
ele1,ele2,ele3,ele4 = new_tuple
print('Value of ele1', ele1)
print(ele1,ele2,ele3,ele4)
