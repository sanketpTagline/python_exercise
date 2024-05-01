class BankAccount:
    def __init__(
        self, account_holder_name, account_number, account_balance, account_pin):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_pin = account_pin

    def deposit(self):
        while self.check_pin():
            print("Sorry, Please Enter Correct Pin.")
            self.check_pin()
        else:
            amount = int(input("Enter the Deposit amount:"))
            self.account_balance = self.account_balance + amount
            print(f"{amount}$ rupees are successfully added to your account.")
            self.__str__()

    def withdraw(self):
        while self.check_pin():
            print("Sorry, Please enter correct pin.")
            self.check_pin()
        else:
            amount = int(input("Enter the Deposit amount:"))
            if self.account_balance >= amount:
                self.account_balance -= amount
                self.__str__()
            else:
                print("Your account dont have sufficient balance")

    def __str__(self):
        print("\n")
        print("Account Holder Name:", self.account_holder_name)
        print("Account Number:", self.account_number)
        print("Account Balance:", self.account_balance)

    def check_pin(self):
        pin = int(input("Enter your account pin :"))
        if self.account_pin != pin:
            self.check_pin()


b1 = BankAccount("Ram", "12345", 10000, 1234)

print("\n ----- ----- Bank Account Detail ----- ----- \n")
print("Select Any one Option:")

print("\n 1. Deposit Amount")
print("\n 2. Withdraw Amount")
print("\n 3. Display Account Details")

option_select = int(input("Select the option number :"))
match option_select:
    case 1:
        b1.deposit()
    case 2:
        b1.withdraw()
    case 3:
        b1.__str__()
    case _:
        print("Plase Enter Properly Number")
