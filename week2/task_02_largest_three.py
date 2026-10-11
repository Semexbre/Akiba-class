number_1 = float(input("Enter your first number"))
number_2 = float(input("Enter your second number"))
number_3 = float(input("Enter your third number"))

if number_1 > number_2 and number_1 > number_3:
    print(f"number {number_1} is the largest")
elif number_2 > number_1 and number_2 > number_3:
    print(f"number {number_2} is the largest")
elif number_2 == number_1 == number_3:
    print("all the three numbers are equal")
else:
    print(f"number {number_3} is the largest")