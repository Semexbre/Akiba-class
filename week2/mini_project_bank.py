
# basic ccount information
correct_pin = "1234"
balance = 1000
transactions = 0

## pin verifcation
attempts = 3
access_granted = False

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.")
        access_granted = True
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")

        if attempts > 0:
            print("Attempts remaining:", attempts)

if not access_granted:
    print("Too many incorrect attempts.")
    print("Your account is locked.")

else:
    ## bank menu
    while True:
        print("\n===== AKIBA BANK =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        # choice 1 Check balance
        if choice == "1":
            print("Your current balance is:", balance, "Birr")

        # choice 2 Deposit money
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance += amount
                    transactions += 1

                    print("Deposit successful!")
                    print("Your new balance is:", balance, "Birr")
                else:
                    print("Invalid amount.")
                    print("Deposit must be greater than zero.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # choice 3 withdrawal money
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid amount.")
                    print("Withdrawal must be greater than zero.")

                elif amount > balance:
                    print("Insufficient balance!")

                else:
                    balance -= amount
                    transactions += 1

                    print("Withdrawal successful!")
                    print("Your new balance is:", balance, "Birr")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # exit option
        elif choice == "4":
            print("Transactions made:", transactions)
            print("Thank you for using Akiba Bank!")
            print("Goodbye!")
            break

        # Invalid menu option
        else:
            print("Invalid option.")
            print("Please choose a valid option.")
