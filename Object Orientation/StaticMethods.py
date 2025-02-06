class MathOperations:
    @staticmethod    #decorator
    def add_number(a,b):
        return a+b
    def calci(self):
        pass
result = MathOperations.add_number(5,3) #without creating object
print(result)

math_op = MathOperations()
print(math_op.add_number(10,5)) #with creation of object
