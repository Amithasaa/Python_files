li = input('Enter space seperated elements')
print(li,type(li)) #10 20 30 <class 'str'>
li = li.split()
print(li) #['10', '20']
li = list(map(int,li))
print(li) #[10, 20, 30]

#In one line
tup = tuple(map(int,input('Enter space seperated elements ').split()))
print(tup) #(10, 20, 30)


print('k o d n e s t'.split()) #['k', 'o', 'd', 'n', 'e', 's', 't']
print('k-o-d'.split()) #['k-o-d']

li = list(map(int,input().split()))
print([i for i in li if i%2==0])