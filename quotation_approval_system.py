amount = float(input("Enter the amount for the quotation: "))


if amount <= 50000:
    print("Quotation Auto approved")
else:
    print("Manager Approval Required")

manager_approval = input("Did the manager approved? (yes/no): ")

if manager_approval == "yes":
        print("Director Approval Required")

        director_approval = input("Did the director approved? (yes/no): ")
        if director_approval == "yes":
            print("Quotation final approved")
        else:
            print("Quotation rejected by Director")

else:
    print("Quotation rejected by Manager")