<<<<<<< HEAD
'''
1.Conditional : if-else, if-elif
2.Looping: for,while
3.Jumping: break, continue, pass
'''

#if-else
def checkAge(age):
    if (age>18):
        print("Age is greater than 18")
    else:
        print("Age is not greater than 18")
checkAge(18)

#if-elif
def ageCheck(age):
    if(age<18):
        print("Child")
    elif(age>18):
        print("Adult")
    elif(age>60):
        print("Senior Citizen")
    else:
        print('No age')
ageCheck(int(input("Enter age")))
=======
'''
1.Conditional : if-else, if-elif
2.Looping: for,while
3.Jumping: break, continue, pass
'''
def checkAge(age):
    if (age>18):
        print("Age is greater than 18")
    else:
        print("Age is not greater than 18")
checkAge(18)

#if-elif
def ageCheck(age):
    if(age<18):
        print("Child")
    elif(age>18):
        print("Adult")
    elif(age>60):
        print("Senior Citizen")
    else:
        print('No age')
ageCheck(int(input("Enter age")))
>>>>>>> 6729aa240a7a25022ef447f4c282c6c15ddfe66b
