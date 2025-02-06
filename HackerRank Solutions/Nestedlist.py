'''
li = []
n = int(input()) #number of students
for i in range(n):
    name = input()
    score = float(input())
    li.append([name, score])
#print(li) [['s', 23.0], ['4', 34.0]]
scores = []
for name, score in li:
    scores.append(score)
scores = list(set(scores))
scores.sort()
name_li = []
second_smallest = scores[1]
for name, score in li:
    if score == second_smallest:
        name_li.append(name)
name_li.sort()
for name in name_li:
    print(name)
'''

li = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    li.append([name, score])
scores = []
for name, score in li:  #unpacking the score
    scores.append(score)
scores = list(set(scores))
scores.sort()
name_li = []
second_lowest = scores[1]
for name, score in li:
    if score == second_lowest:
        name_li.append(name)
name_li.sort()
for name in name_li:
    print(name)


