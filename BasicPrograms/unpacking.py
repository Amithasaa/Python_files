#unpacking
#multiple values in marks so use *
name,*marks = ['pooja',10,20,30]
print(name)
print(marks)

#2nd
name,*marks,age = ['Rahul',100,40,50,23]
print("Name:",name)
print("Marks:",marks)
print("Age:",age)

#3rd
name,age,*marks = ['Rahul',12,40,50,80]
print("Name:",name) 
print("Age:",age)
print("Marks:",marks)



