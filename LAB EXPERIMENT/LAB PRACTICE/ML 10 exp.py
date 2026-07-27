fare = float(input("Enter ticket fare: "))
age = int(input("Enter age: "))
cls = input("Enter class (First/Second): ")

if age < 12:
    fare *= 0.5
elif age >= 60:
    fare *= 0.7

if cls == "First":
    fare += 200

print("Total Fare =", fare)
