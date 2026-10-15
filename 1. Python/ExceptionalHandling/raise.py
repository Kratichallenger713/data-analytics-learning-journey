age = int(input("Enter Age: "))

if age < 18:
    raise Exception("Age Must Be 18+")

print("Eligible")