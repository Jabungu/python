class Bankaccount:
    def __init__(self, int_rate, balance):
        self.int_rate = 0.01
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('not enough funds')
            self.balance -= 5
        return self

    def display_info(self):
        print(str('balance is $'), self.balance)
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self


account1 = Bankaccount(0.5, 100)
account1.deposit(10).deposit(20).deposit(20).withdrawal(10).yield_interest().display_info()

print(account1)
