lis = list(map(int,input().split(",")))
lis = list(set(lis)) #removes duplicates
#lis = lis.sort() ---Error: sort method won't return anything so it will return none
lis.sort()
print(lis[1])
print(lis[-1]) #largest value
print(lis[-2]) #second largest value

