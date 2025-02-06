'''
The variables which are public can be accessed inside the same class, 
outside of any class, inside the child class and inside non-child class
'''

class Demo1:
    def __init__(self,name):
        self.name = name
    
    def disp1(self):
        print(self.name)
        
d1 = Demo1('Akash')
print(d1.name)
d1.disp1()

class Demo2(Demo1):
    pass

    def disp2(self):
        print(self.name)

d2 = Demo2('Pooja')
print(d2.name)
d2.disp2()