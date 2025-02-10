li = [10,20,30,40]
print(type(li),li)
li = iter(li)
print(type(li),li)

print(next(li))
print(next(li))
print(next(li))
print(next(li))
#print(next(li)) # stop iteration
