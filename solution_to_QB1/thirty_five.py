"""WAP to develop the Banking Application using Menu Driven Approach.
Application should read the customer name, account number,
phone number, address, initial balance and rate of interest
from user. Application should implement following methods.
i) createAccount() ii) deposit() iii) withdraw() iv) checkBalance v) computeInterest()

WAP to calculate the compound interest.
"""

class Customer:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        print(self.balance)

    def compute_intrest(self, r, t):
        n = 100
        A = self.balance * (1 + r / n) ** n * t

        return A
def createAccount(balance):
    return Customer(balance)

if __name__ == "__main__":
    customer_dict = {}
    flag = True
    while flag:
        print("================== TASKS ==================")
        print("1. createAccount")
        print("2. deposit")
        print("3. withdraw")
        print("4. checkBalance")
        print("5. computeInterest")
        task = input("enter the task")
        if task == "createAccount":
            balance, name = input("Enter the (balance, name)").split(", ")
            customer_dict[name] = createAccount(int(balance))
        elif task == "deposit":
            amount, name = input("Enter the (amount, name)").split(", ")
            customer_dict[name].deposit(amount)
        elif task == "withdraw":
            amount, name = input("Enter the (amount, name)").split(", ")
            customer_dict[name].withdraw(amount)
        elif task == "checkBalance":
            name = input("Enter the name")
            customer_dict[name].check_balance()
        elif task == "computeInterest":
            r, t, name = input("Enter the (Rate of interest, number of years, name)").split(", ")
        elif task == "done":
            flag = False
        else:
            print("Invalid Input")