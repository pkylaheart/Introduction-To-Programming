def add_funds(account_balance, deposit_amount):
    account_balance += deposit_amount
    print(f"Funds added: ₱{deposit_amount}")
    return account_balance

def remove_funds(account_balance, withdrawal_amount):
    if withdrawal_amount > account_balance:
        print("Not enough funds!")
    else:
        account_balance -= withdrawal_amount
        print(f"Funds removed: ₱{withdrawal_amount}")
    return account_balance

def bank():
    account_balance = 0
    while True:
        print("\nWelcome to Your Bank Account!")
        print("1. Add Funds")
        print("2. Remove Funds")
        print("3. Check Account Balance")
        print("4. Exit")
        
        user_choice = input("Choose an option (1-4): ")

        if user_choice == "1":
            try:
                deposit_amount = float(input("Enter the amount to add: ₱"))
                if deposit_amount > 0:
                    account_balance = add_funds(account_balance, deposit_amount)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif user_choice == "2":
            try:
                withdrawal_amount = float(input("Enter the amount to remove: ₱"))
                if withdrawal_amount > 0:
                    account_balance = remove_funds(account_balance, withdrawal_amount)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif user_choice == "3":
            print(f"Your current balance is: ₱{account_balance}")
        
        elif user_choice == "4":
            print("Thanks. See you next time!")
            break
        
        else:
            print("Invalid choice! Please select a valid option (1-4).")

bank()
