role = input("Enter your role")
if role == "admin" or role == "manager":
    print("Access granted")

else:
    print("Access denied")
    print(role)
    print(repr(role))
    print(role == "admin")