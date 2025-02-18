# from functools import reduce
# li = [1,2,3,4,5]
# newli = list(filter(lambda num : num % 2 == 0, li))
# print(newli) #[2, 4]

# sum = reduce(lambda a,b: a+b,li)
# print(sum) #15

# square = list(map(lambda num: num**2, li))
# print(square) #[1, 4, 9, 16, 25]

arr = []
n = int(input("Enter the size of the array: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)
print("Array:", arr)
key = int(input())
for i in range(n):
    if arr[i] == key:
        print("key found")
    return arr[i]
print("key not found")
    