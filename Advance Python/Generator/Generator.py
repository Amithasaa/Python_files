# def disp():
#     return 10
#     return 20
#     return 30
# res = disp()
# print(disp())
# print(disp())
# print(res)

def generator_function():
    yield 10
    yield 20
    yield 30

gen = generator_function()
print(generator_function()) # object   <generator object generator_function at 0x00000286A5404B40>    
print(next(gen)) #10
print(next(gen)) #20
print(next(gen)) #30
# print(next(gen)) StopIteration
  
