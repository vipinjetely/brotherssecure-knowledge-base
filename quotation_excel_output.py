from openpyxl import Workbook

client_name = input("Enter client name: ")
amount = float(input("Enter amount: "))

workbook = Workbook()

sheet = workbook.active
sheet.title = "Quotation"

sheet["A1"] = "Client Name"
sheet["B1"] = "Amount"

sheet["A2"] = client_name
sheet["B2"] = amount

workbook.save("quotation_status.xlsx")

print("Quotation Excel created successfully")