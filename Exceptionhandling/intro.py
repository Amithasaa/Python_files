'''
1.try: Used to keep the logic in which we get occur some error
2.except: It will be excecuted when exception occurs in try block logic
3.else: will be excecuted when try block logic  will be excecuted without any error
4.finally : will always be excecuted irrespective of exception occured or not
'''

def disp(a,b):
    try:
        print('Task Started')
        print(a/b) # ZeroDivisionError: division by zero
        
    except:
        print('Some error handled')
    else:
        print('Task excecuted without any exception')
    finally:
        print('Task ended')
disp(10,0)
disp(10,5)
disp(20,2)

