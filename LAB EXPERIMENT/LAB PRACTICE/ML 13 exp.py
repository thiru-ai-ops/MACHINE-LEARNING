hours = int(input("Enter parking hours: "))
vehicle = input("Enter vehicle (Bike/Car): ")

if vehicle == "Bike":
    fee = hours * 20
else:
    fee = hours * 50

print("Parking Fee = Rs.", fee)
