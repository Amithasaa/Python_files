#In this code we are achieving polymorphism using method overriding
class Calculator:
    def calculate(self, a, b):
        pass
        
class Add(Calculator):
    def calculate(self, a, b):
        print('Addition:', a+b)
        
class Sub(Calculator):
    def calculate(self, a, b):
        print('Subtraction:', a-b)
        
class Mul(Calculator):
    pass
 

ref = Add()
ref.calculate(10,20) #Addition: 30

ref = Sub()
ref.calculate(60,50) #Subtraction: 10

ref = Mul()
ref.calculate(10,20)


