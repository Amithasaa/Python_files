'''1.Strings are immutable : Once we declare a string we cannot modify it
if we try to modify a string it will create new strimg
2.If new string does not have any reference variable then it will be removed.
3.Python internally uses string interning
4.String interning is the process of checking string intern pool before creating 
any new object
5.Whenever we want to crete new object, python first will check string intern pool whether that object already exist or not
when object already exist in the string intern records then address of existing object will be reused'''
s1 = 'kodnest'
s1 = s1.upper()
print(s1) 

#To check the address we use id()
s1 = 'K'
print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1,id(s1))
print(s2,id(s2))
print("s1 Id of H:", id(s1[0])) #H
print("s2 Id of W:",id(s2[0]))

print("s1 Id of o:", id(s1[-1])) #o
print("s2 Id of o:",id(s2[1]))

print("s1 Id of l:",id(s1[2]))
print("s1 Id of l:",id(s2[3]))
print("s2 Id of l:",id(s2[3]))