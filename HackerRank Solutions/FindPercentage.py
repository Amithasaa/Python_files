'''
d = {}
n = int(input())
for i in range(n):
    name, *score = input().split() #['Abc' ,10','20','30']
    score = list(map(float,score))
    d[name] = score
target_name = input()
for name,score in d.items():
    if name == target_name:
        avg = sum(score)/len(score)
print(f"{avg: .2f}")
'''

d = {}
n = int(input())
for i in range(n):
    name, *score = input().split()
    score = list(map(float,score))
    d[name] = score
target_name = input()
for name, score in d.items():
    if name == target_name:
        avg = sum(score)/len(score)
print(f"{avg:.2f}")