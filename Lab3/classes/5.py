class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        return self.balance

    def withdraw(self, withdrawal):
        if self.balance < withdrawal:
            return True
        else: 
            return False

A = Account('VOLVO', 60000)
B = Account('Lexus',4000000)
print(B.deposit())
print(B.withdraw(7000000))
print(A.deposit())
print(A.withdraw(789000))