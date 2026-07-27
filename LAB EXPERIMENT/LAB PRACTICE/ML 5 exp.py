amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

bill = amount - discount
gst = bill * 0.18
total = bill + gst

print("Discount =", discount)
print("GST =", gst)
print("Total Bill =", total)
