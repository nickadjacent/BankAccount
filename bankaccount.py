class BankAccount:
    def __init__(self, intrate, balance):
        self.intrate = intrate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def displayAccountInfo(self):
        print(self.intrate)
        print(self.balance)
        return self

    def yeildInt(self):
        self.balance += (self.balance*self.intrate)
        return self


user1 = BankAccount(0.01, 100)
user2 = BankAccount(0.01, 5000)

user1.deposit(100).deposit(200).deposit(
    800).withdraw(500).yeildInt().displayAccountInfo()

user2.deposit(5000).deposit(5000).withdraw(250).withdraw(
    250).withdraw(250).withdraw(250).yeildInt().displayAccountInfo()
