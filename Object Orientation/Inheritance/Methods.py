'''
work(): Specialized method : Only in child class
play(): Inherited method : Used as it is in child class
cook(): Overriden method : Change implementation in child class
'''


class Student:
    def cook(self):
        print("Student is cooking")
        
    def play(self):
        print("playing cricket")
        
class Employee(Student):
    def work(self):
        print("Employee is working")
        
    def cook(self):
        print("Employee is cooking")
        
e = Employee()
e.cook()
e.play()
e.work()