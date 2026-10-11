customer_name = input("Enter your name: ")
product_name = input("Enter the product name: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity

print("========================================")
print("                 RECEIPT")
print("========================================")

print(f"Customer: {customer_name}")

print(f"{'Product':<20}{'Price':<10}{'Qty':<5}")
print("----------------------------------------")

print(f"{product_name:<20}{price}{quantity:<5}")
print("----------------------------------------")
print(f"Total: {total} ETB")

print("Thank you for shopping!")
print("========================================")
