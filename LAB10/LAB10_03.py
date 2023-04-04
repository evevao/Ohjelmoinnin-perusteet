#LAB10 tehtävä 03

print("Account has been created.")

dump = input("Press Enter to continue")

class Account:
    def __init__(self, balance):
        self.balance = balance

    def add(self, money):
        self.balance += money
        print("Account balance is:", self.balance, "€")

    def withdraw(self, money):
        if money > self.balance:
            print("Sorry, insufficient amount. You have", self.balance, "€", "withdraw cannot be done.")
        else:
            self.balance -= money

    def account_balance(self):
        return self.balance

tili = Account(2000)
print("The account balance is:", tili.account_balance(), "€")

addedMoney = int(input("How much will be added?: "))
tili.add(addedMoney)
print("The account balance is:", tili.account_balance(), "€")

withdrawnMoney = int(input("How much will be withdrawn?: "))
tili.withdraw(withdrawnMoney)
print("The account balance is:", tili.account_balance(), "€")

withdrawnMoney = int(input("How much will be withdrawn?: "))
tili.withdraw(withdrawnMoney)
print("The account balance is:", tili.account_balance(), "€")

dump = input("Press Enter to continue")

print("Thank you. Come again.")