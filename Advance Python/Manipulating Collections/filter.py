li = [1,2,3,4]
def checkEven(num):
    return num % 2 == 0
res = list(filter(checkEven,li))
print(res)
