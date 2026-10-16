correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter your pin ")

    if pin == correct_pin:
        print("Pin is correct. Welcome")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print("Incorrect pin")
            print("Attempts remaining:", attempts)
        else:
            print("Incorrect pin.")
            print("Your account is locked. No attempts remaining.")