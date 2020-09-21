class bankAccount:
    def __init__(self, rate, balance):
        self.interest = rate
        self.balance = balance
        return self

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    # def withdrawl(self, amount):
    #     if self.balance < amount:
    #         print("Insufficient funds: Charging a $5 fee")
    #         self.balance -=5
    #     else:
    #         self.balance -=amount
    #     return self

    # def displayAccountInfo(self):
    #     print(f"Your current balance is: {self.balance}")
    #     return self

    # def yieldInterest(self):
    #     if self.balance >= 0:
    #         self.balance = self.balance + (self.balance * self.rate)
    #     return self


wellsFargo = bankAccount(.02, 50)
santander = bankAccount(.03, 0)

wellsFargo.deposit(80)


