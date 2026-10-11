name = input("Enter your name: ")
weight = float(input("Enter your weight "))
height = float(input("Enter your height "))

bmi = weight / (height * height)

print("================================")
print("          BMI REPORT")
print("================================")

print(f"Name: {name}")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")

print(f"BMI: {bmi}")

print("================================")
