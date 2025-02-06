class PinError(Exception):
    pass
correctPin = 1212
pin = int(input())
try:
    if(pin == correctPin):
        print("Account unblocked")
    else:
        raise PinError('Entered pin is', pin)
except PinError as e:
    print("Incorrect pin",e)