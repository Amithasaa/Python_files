class Employee:
    company_name = 'code' #class based variable
    def __init__(self, name, age, desig):
        self.name = name
        self.age = age
        self.desig = desig
    def login(self, time):
        print(f"{self.name} logged in at {time}")
        
    def logout(self, time):
        print(f"{self.name} logged out at {time}")
        
    def work(self, hours):
        print(f"{self.name} worked for {hours}")
        
    def get_details(self):
        print('Employee name:',self.name)
        print('Employee age:',self.age)
        print('Employee designation:',self.desig)
        
 #creating objects       
e1 = Employee("Amitha", 22, "Developer")
e2 = Employee("Arpitha", 21, "Engineer")

print("Details of Employee 1:")
e1.get_details()
e1.login("7 AM")
e1.logout("6 PM")
e1.work("9 Hours")

print("-----------------------------------------")

print("Details of Employee 2:")
e2.get_details()
e2.login("8 AM")
e2.logout("9 PM")
e2.work("8 hours")