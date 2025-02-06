'''
class Demo1:
    def disp1(self):
        print("Inside disp1")

class Demo2:
    def disp(self):
        print("Inside disp2 of Demo2")
        
class Demo3(Demo1, Demo2):
    pass

d3 = Demo3()
d3.disp() #Inside disp2 of Demo2
'''

class Demo1:
    def __init__(self):
        self.x = 100
        
class Demo2:
    def __init__(self):
        self.x = 200

class Demo3(Demo2, Demo1):
    def __init__(self):
        self.x = 300
        
d3 = Demo3()
print(d3.x)