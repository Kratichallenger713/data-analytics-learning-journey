bill = int(input("Enter Bill Amount: "))

if bill > 1000:
    discount = bill * 0.10
    print("Discount =", discount)
else:
    print("No Discount")

