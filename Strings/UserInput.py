#Input method is always takes an input as a string
#division output is always float type
num1 = int(input("Enter a num1\n"))
print("The value of num1 is:",num1, "Data type of num is:",type(num1))

num1 = int(input("Enter a num1\n"))
num2 = int(input("Enter a num2\n"))
result = num1 + num2
print(f"Addition of {num1} and {num2} is:", result)
print(f'Subtraction of {num1} and {num2} is:', num1-num2)
print(f'Multiplication of {num1} and {num2} is:', num1*num2)
print(f'Division of {num1} and {num2} is:', num1/num2)  