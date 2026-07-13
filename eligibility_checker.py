age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: "))

if age >= 25 and experience >= 2:
    print("Selected for interview.")    

elif age > 21 and experience == 0:
    print("fresher Candidate")

else:
    print("Not eligible.")