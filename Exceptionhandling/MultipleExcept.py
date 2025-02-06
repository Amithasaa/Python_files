def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Zero division error occured and handled')
    except NameError:
        print('Name error occured and handled')
    except TypeError:
        print("type error occured and handled")
    except ValueError:
        print("Value error occured and handled")
    except:
        print('Some error occured and handled')
a = int(input()) 
b = int(input())       
disp(a,b)