client = input("Enter client name: ")
item = input("Enter item name: ")

qty = int(input("Enter quantity: "))
rate = float(input("Enter rate: "))

amount = qty * rate
gst = amount * 0.18
grand_total = amount + gst

print("Client Name:", client)
print("Item Name:", item)
print("Quantity:", qty)
print("Rate:", rate)
print("Amount:", amount)
print("GST 18% :", gst)
print("Grand Total:", grand_total)