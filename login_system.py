username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username and password match the stored credentials
if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Invalid username or password.")