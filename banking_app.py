class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")


class SavingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

if __name__ == "__main__":
    savings = SavingAccount("55555", "Azwan", 1000)

    print(f"Account Holder: {savings.account_holder}")
    print(f"Account Number: {savings.account_number}")
    print(f"Initial Balance: {savings.balance}")

    savings.deposit(500)
    print(f"After Deposit: {savings.balance}")

    interest = savings.calculate_interest()
    print(f"Interest: {interest}")

    savings.withdraw(300)
    print(f"After Withdrawal: {savings.balance}")

    interest = savings.calculate_interest()
    print(f"Interest: {interest}")

    savings.withdraw(1500) 
    print(f"After Withdrawal Attempt: {savings.balance}")

    interest = savings.calculate_interest()
    print(f"Final Interest: {interest}")
