#Different ways of declaring strings:
s1 = 'My name is Amitha'
s2 = 'My "age" is 22'
s3 = """We are learning Strings"""
s4 = '''Python is dynamically typed language'''
print(s1)
print(s2)
print(s3)
print(s4)

#Accessing a characters in a string
words = "Python"
print(words[0])
print(words[4])
print(words[-1])
print(words[-3])

#Slicing strings
greeting = "hello, Python"
print(greeting[0:7])
print(greeting[1:8])
print(greeting[3:])

#Length of a string
word = 'Hello'
print(len(word))
message = "Welcome to Python!"
print(len(message))

#Changing the case of the string
text = "Hello, World!"
print(text.upper())
print(text.lower())

#Finding substrings in a string
test = "Learning Python is fun!"
print(test.find("Python"))
print("fun" in test)

#Replacing a part of the string
sentence = "I like Java."
new_sentence = sentence.replace("Java","python")
print(new_sentence)

#Splitting and Joining
text = "apple, banana, cherry"
fruit = text.split(",")
print(fruit)
joined_text = "-".join(fruit)
print(joined_text)

#Strip method
msg = '  Hello Python!  '
stripped_msg = msg.strip()
print(stripped_msg)