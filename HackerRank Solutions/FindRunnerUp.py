n = int(input())
arr = list(map(int,input().split()))
arr = list(set(arr))
arr.sort(reverse=True) # descending order
print(arr[-2]) #last 2nd index

n = int(input())
arr = list(map(int,input().split()))
arr = list(set(arr))
arr.sort() #ascending order
print(arr[1]) #1st index value