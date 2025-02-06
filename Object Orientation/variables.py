class Bank:
    bank_name = 'SBI'
    def __init__(self,name,age,balance):
        self.name = name
        self.age = age
        self.balance = balance
        
    def get_info(self):
        print(f'''User name is: {self.name} and User balance: {self.balance} for Bank: {Bank.bank_name}''') # or {self.bank_name}
        
        
b1 = Bank("Pooja",25,5000)

print(b1.bank_name) #SBI
print(Bank.bank_name) #class based variables #SBI
b1.get_info()

