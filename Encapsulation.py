# 2.Build a Secure Banking System using Encapsulation
# Design a BankAccount class that:
# • Has a private variable __balance.
# • Provides methods deposit(amount), withdraw(amount), and get_balance().
# • Ensures balance cannot be accessed directly from outside the class.
# • Create a SavingsAccount class that inherits from BankAccount and adds
# interest_rate functionality.
#  Test Cases:
# • Create an account, deposit money, withdraw money, and check the balance.
# • Try accessing __balance directly and note the error.

class BankAccount:
    def __init__(self):
        self.__balance=0.0
    def deposit(self,amount):
        if amount >0:
            self.__balance+=amount
            print("Deposited: ${}.New balance: ${}".format("%0.2f" %amount,"%0.2f" %self.__balance))
        else:
            print("Deposit amount must be positive.")
    def withdraw(self,amount):
        if 0< amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.__balance:.2f}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")
    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, interest_rate):
        super().__init__()
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"Applied interest: ${interest:.2f}. New balance: ${self.get_balance():.2f}")

# Test Cases
if __name__ == "__main__":
    savings_account = SavingsAccount(interest_rate=5)

    savings_account.deposit(1000)

    savings_account.withdraw(200)

    print(f"Current balance: ${savings_account.get_balance():.2f}")

    savings_account.apply_interest()
    try:
        print(savings_account.__balance)
    except AttributeError as e:
        print(f"Error: {e}")