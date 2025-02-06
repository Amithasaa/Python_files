#isalnum() : Check for alphabets or numbers
s1 = "kodnest"
print(s1.isalnum())  #True //Either alphabets or numbers
s1 = "kodnest123"
print(s1.isalnum()) #True
s1 = "kodnest12#"
print(s1.isalnum()) #false

#isalpha() : Check for alphabets
print("kodnest".isalpha()) #true
print("kodnest123".isalpha()) #false

#isdigit() : Check for digits
print("1234".isdigit()) #True
print('12AB'.isdigit()) #false

#islower() : check for lowercase characters
print("abcdef".islower()) #True
print("abcdef123".islower()) #true
print("Abcdef".islower()) #False

#isupper() : Check for uppercase characters
print("ABCDEF".isupper()) #True
print("ABCD12".isupper()) #True
print("abcDEF".isupper()) #false
print("ABC#$".isupper()) #true

print(any((10,20,30))) #True
print(any([True,False,False])) #True
print(any([False,False])) #False

print("---------------------------------------")
s = input()
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.isupper() for i in s]))
print(any([i.islower() for i in s]))

