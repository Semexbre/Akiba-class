usdt_amount = float(input("Enter usdt amount"))
rate = 150

usdt_to_birr = usdt_amount * rate

print("==============================")
print("   CURRENCY EXCHANGE")
print("==============================")

print(f"USD Amount: {usdt_amount}")
print(f"Exchange Rate: 1 USD = {rate} ETB")
print(f"ETB Amount: {usdt_to_birr} ETB")
print("==============================")