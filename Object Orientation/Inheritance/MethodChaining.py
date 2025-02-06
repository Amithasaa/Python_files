'''
Method chaining is the process of calling one method from another method.
'''

class GrandParent:
    def cook(self):
        print("Grand Parent can cook")
        
class Parent(GrandParent):
    def cook(self):
        print("Parent can cook")
        
class Child(Parent):
    def cook(self):
        print("Child won't cook")
        super().cook()
        super(Parent,self).cook()
        
c = Child()
c.cook()