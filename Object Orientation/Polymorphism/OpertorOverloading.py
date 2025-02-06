class Demo1:
    def __str__(self):
        return 'Hello'
    
    def __add__(self, other):
        self.a = 10
        other.b = 20
        return self.a + other.b

class Demo2:
    
    def __str__(self):
        return 'Hi'

d1 = Demo1()
d2 = Demo2()
print(d1)
print(d2) 
print(d1 + d2)

'''<__main__.Demo1 object at 0x000002597C7E73B0> In python if we print reference 
variable then internally python will envoke __str__() which always returns string 
representation of an address of an object.

In the above examples we have overridden __str__ methods in their respective classes

Dunder methods: The methods which has suffix and prefix as double underscore(__)
These dunder methods are called as magic methods because as programmer we no need to call any methods,
automatically methods will be invoked.
'''
