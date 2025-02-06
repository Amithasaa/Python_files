# print('a'.islower())
# print('kodnest'.isupper())

def swapcase(s):
    sample = ''
    s = input()
    for i in s:
        if i.islower():
            sample = sample + i.upper()
        else:
            sample = sample + i.lower()
    return sample
res = swapcase('PythoN12')
print(res)