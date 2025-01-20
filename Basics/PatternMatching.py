<<<<<<< HEAD
# 5 * 4 Rectangle
rows = 5
columns = 5
for i in range(rows):
    for j in range(columns):
        print("* ", end='')
    print()

# right angle increasing direction
for i in range(4):
    for j in range(i+1):
        print('*', end='')
    print()

#right angle decreasing direction
for i in range(rows):
    for j in range(i,rows):
        print('*', end='')
    print()
    
#increasing and decreasing pattern pascal triangle
# 4 stars twice
for i in range(rows):
    for j in range(i+1):
        print('* ', end='')
    print()
for i in range(rows):
    for j in range(i,rows):
        print('* ', end='')
    print()

print()

# only once 4 stars
for i in range(rows):
    for j in range(i+1):
        print('* ', end='')
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print('* ', end='')
    print()
    
#Butterfly pattern
for i in range(rows):
    for j in range(i+1):
        print('*', end='')
    for j in range(i,rows-1):
        print(' ', end="")
    for j in range(i,rows-1):
        print(' ', end="")
    for j in range(i+1):
        print('*', end="")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print('*', end='')
    for j in range(i+1):
        print(' ', end="")
    for j in range(i+1):
        print(' ', end="")
    for j in range(i,rows-1):
        print('*', end="")
    print()
    
    #rhombus
for i in range(5):
    for j in range(i,rows):
        print(' ', end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(1,rows):
    for j in range(i+1):
        print(' ', end="")
    for j in range(i,rows):
        print("*",end="")
    for j in range(i,rows-1):
        print('*',end='')
=======
# 5 * 4 Rectangle
rows = 5
columns = 5
for i in range(rows):
    for j in range(columns):
        print("* ", end='')
    print()

# right angle increasing direction
for i in range(4):
    for j in range(i+1):
        print('*', end='')
    print()

#right angle decreasing direction
for i in range(rows):
    for j in range(i,rows):
        print('*', end='')
    print()
    
#increasing and decreasing pattern pascal triangle
# 4 stars twice
for i in range(rows):
    for j in range(i+1):
        print('* ', end='')
    print()
for i in range(rows):
    for j in range(i,rows):
        print('* ', end='')
    print()

print()

# only once 4 stars
for i in range(rows):
    for j in range(i+1):
        print('* ', end='')
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print('* ', end='')
    print()
    
#Butterfly pattern
for i in range(rows):
    for j in range(i+1):
        print('*', end='')
    for j in range(i,rows-1):
        print(' ', end="")
    for j in range(i,rows-1):
        print(' ', end="")
    for j in range(i+1):
        print('*', end="")
    print()
for i in range(rows):
    for j in range(i,rows-1):
        print('*', end='')
    for j in range(i+1):
        print(' ', end="")
    for j in range(i+1):
        print(' ', end="")
    for j in range(i,rows-1):
        print('*', end="")
    print()
    
    #rhombus
for i in range(5):
    for j in range(i,rows):
        print(' ', end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print('*',end='')
    print()
for i in range(1,rows):
    for j in range(i+1):
        print(' ', end="")
    for j in range(i,rows):
        print("*",end="")
    for j in range(i,rows-1):
        print('*',end='')
>>>>>>> 6729aa240a7a25022ef447f4c282c6c15ddfe66b
    print()