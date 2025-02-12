from functools import reduce
li = [1,2,3,4]
def mul(a,b):
    return a*b

res = reduce(mul,li)
print("Multiplication is:", res)
#Multiplication is: 24