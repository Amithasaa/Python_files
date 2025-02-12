def decorator(func):
    def inner(numerator,denominator):
        if denominator == 0:
            print("Denominator is holding zero")
        else:
            func(numerator, denominator)
            
    return inner

@decorator
def div(numerator, denominator):
    print("divisible", numerator/denominator)
    
div(10,20)
div(10,0)