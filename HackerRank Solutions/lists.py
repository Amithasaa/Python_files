'''
li = []
n = int(input())
for i in range(n):
    command,*values = input().split() #'remove 30' remove in command and 30 as a list in values
    values = list(map(int,values)) # covert string to integer values
    if (command == 'insert'):
        li.insert(values[0], values[1]) #[0,100] 0th index 100 value is placed
    elif (command == 'print'):
        print(li)
    elif (command == 'remove'): # removes 0th index
        li.remove(values[0])
    elif (command == 'append'):
        li.append(values[0])  # appends the value at 0th index
    elif (command == 'sort'):
        li.sort()
    elif (command == 'pop'):
        li.pop()
    elif (command == 'reverse'):
        li.reverse()
'''

li = []
n = int(input())
for i in range(n):
    command, *values = input().split()
    values = list(map(int, values))
    if command == 'insert':
        li.insert(values[0], values[1])
    elif command == 'print':
        print(li)
    elif command == 'remove':
        li.remove(values[0])
    elif command == 'append':
        li.append(values[0])
    elif command == 'sort':
        li.sort()
    elif command == 'pop':
        li.pop()
    elif command == 'reverse':
        li.reverse()
        