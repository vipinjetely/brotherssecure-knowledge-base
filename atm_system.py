balance = 50000
amount = int(input("Enter withdraw amount: "))
invalid_amount = amount < 0 or amount > balance

if not invalid_amount and amount <= balance:
    print("Transaction Successful")
    print("Remaining balance: ₹" + str(balance - amount))
else:
    print("Invalid Amount") 