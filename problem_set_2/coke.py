total_payment = 0
while total_payment < 50:
    print("Amount Due:", 50 - total_payment)
    payment = int(input("Insert coin: "))
    if payment == 25 or payment == 10 or payment == 5:
        total_payment += payment
print("Change Owed:", total_payment - 50)
