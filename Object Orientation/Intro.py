class Student:
    def learn(self):
        print(self.name,"is learning method")
    def play():
        print("Inside play method")
s1 = Student()
s1.name = 'Pooja'
print('Name is', s1.name)
print(s1.learn())
# print(s1.play()) #takes 0 positional arguments but 1 was given self
