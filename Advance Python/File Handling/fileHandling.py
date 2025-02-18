file = open('test.txt', 'r')
print(file.read())
print(file.readline())
# print(firstline)
print(file.readlines())
file.close()
# print(data)


file1 = open("test2.txt", 'a')
file1.write("Hello from java")
file1.write("Hello from python")
file1.write("Hello from java")
file1.close()

with open('test.txt', 'r') as file:
    content = file.read()
    print(content)