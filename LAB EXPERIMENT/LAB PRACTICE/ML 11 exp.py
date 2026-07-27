d = float(input("Enter distance (km): "))
m = float(input("Enter mileage (km/l): "))
p = float(input("Enter fuel price (Rs/l): "))

cost = (d / m) * p

print("Fuel Cost = Rs.", cost)
