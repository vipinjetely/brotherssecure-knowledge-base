client = input("Enter client name: ")
item = input("Enter item name: ")
qty = int(input("Enter quantity: "))
rate = float(input("Enter rate: "))
amount = qty * rate
discount = 0.0
if amount > 1000:
    discount = amount * 0.1  # 10% discount for amounts greater than 1000
final_amount = amount - discount
print(f"Final Amount: {final_amount}")