class User:
    def _init_(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        self.account_balance -= amount



user1 = User("Lebron", "lbj@nba.com")
user2 = User("Kobe", "mamba@nba.com")
user3 = User("Trae", "trae@nba.com")

user1.make_deposit(5)
user2.withdraw(3)