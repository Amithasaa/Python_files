num = int(input())
width =len(bin(num))-2
for i in range(1,num+1):
    dec = str(i).rjust(width)
    ot = oct(i)[2:].rjust(width)
    he = hex(i)[2:].upper().rjust(width)
    binary = bin(i)[2:].rjust(width)
    print(f'{dec} {ot} {he} {binary}')
    
# print(f'Binary of {num} is: {bin(num)}')
# print(f'Octal of {num} is: {oct(num)}')
# print(f'hex of {num} is: {hex(num)}')
