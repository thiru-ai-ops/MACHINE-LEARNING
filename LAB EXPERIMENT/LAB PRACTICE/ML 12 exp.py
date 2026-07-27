amount = float(input("Enter recharge amount: "))

if amount >= 500:
    cashback = 100
elif amount >= 300:
    cashback = 50
else:
    cashback = 0

final = amount - cashback

print("Cashback = Rs.", cashback)
print("Final Amount = Rs.", final)
