employee_name = input("Enter your name")
salary = float(input("Enter your salary"))
transport = float(input("Enter your transport allowance"))
food = float(input("Enter your food allowance"))

Gross_salary = salary +  transport + food

print("========================================")
print("          EMPLOYEE PAYSLIP")
print("========================================")


print(f"Employee : {employee_name}")
print(f"Basic Salary : {salary:<10} ETB")
print(f"Transport Alowance : {transport:<10} ETB")
print(f"Food Allowance: {food:<10} ETB")
print("----------------------------------------")
print(f"Gross Salary: {Gross_salary:<10} ETB")
print("========================================")