class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")

def main():
    atm = ATM(1000)
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Select option: ")
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amt = float(input("Enter deposit amount: "))
            atm.deposit(amt)
        elif choice == '3':
            amt = float(input("Enter withdrawal amount: "))
            atm.withdraw(amt)
        elif choice == '4':
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()