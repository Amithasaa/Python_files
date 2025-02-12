def fibonacci_gen(num):
    x,y = 0,1
    for i in range(num):
        yield x
        x,y = y, x+y
ref = fibonacci_gen(10)
#one way
print(ref)
for i in ref:
    print(i)
    
#2nd way
for i in range(5):
    print(next(ref))
    
#3rd way
print(next(ref))

#4th way
print(ref.__next__())
        