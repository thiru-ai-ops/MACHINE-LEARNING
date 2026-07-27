seats = int(input("Enter number of seats: "))
cat = input("Enter category (Silver/Gold): ")

price = 150 if cat == "Silver" else 250
total = seats * price

if seats >= 5:
    total *= 0.9

print("Total Ticket Cost = Rs.", total)
