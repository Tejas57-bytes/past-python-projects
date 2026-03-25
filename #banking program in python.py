#banking program in python

def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit(balance, amount):
    if amount <= 0:
        print("Deposit amount must be positive.")
    else:
        balance += amount
        print(f"Deposited ${amount:.2f}.")
    return balance

def withdraw(balance, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount > balance:
        print("Insufficient funds for this withdrawal.")
    else:
        balance -= amount
        print(f"Withdrew ${amount:.2f}.")
    return balance

def main():
    balance = 0.0
    while True:
        print("\nWelcome to the Banking Program!")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Please choose an option (1-4): ")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)
        elif choice == '4':
            print("Thank you for using the Banking Program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()