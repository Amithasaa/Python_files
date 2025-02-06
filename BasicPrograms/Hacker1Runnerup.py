#Find runner-up score
li = list(map(int,input().split()))
li = [10,20,40,30]
li = list(set(li))
li.sort(reverse=True)
print(li) #[10,20,30,40]
print(li[1])

