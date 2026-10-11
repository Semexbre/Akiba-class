x = int(input("Enter your number"))

if x < 2:
    print("Your number is not prime")
else:
    y = 2

    while y < x:
        if x % y == 0:
            print("Your number is not prime")
            break
        y += 1
    else:
        print("Your number is prime")
