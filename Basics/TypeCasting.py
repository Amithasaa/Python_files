<<<<<<< HEAD
#If string is holding integer than it can be converted into int
a = '30'
b = int(a)
print(a, type(a))
print(b, type(b))

#string to integer conversion is not allowed
x = 'kod'
print(x,type(x))
y = int(x)
print(y, type(y))

p = float(input("Enter float type data"))
print(p, type(p))

#bool()
#While converting int to bool for all non zero values we will get true
#While converting int to bool for a 0 and empty strings we will get false
q = '' #0, 89
q = bool(q)
print(q, type(q))

#
print(bool('Kodnest')) #true
print(int('kod')) #error
print(int('11')) # Imp str(int) -> int
print(float('Kodnest')) #error
print(float('22.22')) # 22.22 imp
print(bool('')) #false
print(bool(0)) #false
print(bool(18)) #true
print(int('12.56')) #error
print(int(12.56)) # 12

#Taking float value from user and converting it into int
value = int(float(input("Enter float value")))
print(value, type(value))
=======
#If string is holding integer than it can be converted into int
a = '30'
b = int(a)
print(a, type(a))
print(b, type(b))

#string to integer conversion is not allowed
x = 'kod'
print(x,type(x))
y = int(x)
print(y, type(y))

p = float(input("Enter float type data"))
print(p, type(p))

#bool()
#While converting int to bool for all non zero values we will get true
#While converting int to bool for a 0 and empty strings we will get false
q = '' #0, 89
q = bool(q)
print(q, type(q))

#
print(bool('Kodnest')) #true
print(int('kod')) #error
print(int('11')) # Imp str(int) -> int
print(float('Kodnest')) #error
print(float('22.22')) # 22.22 imp
print(bool('')) #false
print(bool(0)) #false
print(bool(18)) #true
print(int('12.56')) #error
print(int(12.56)) # 12

#Taking float value from user and converting it into int
value = int(float(input("Enter float value")))
print(value, type(value))
>>>>>>> 6729aa240a7a25022ef447f4c282c6c15ddfe66b
