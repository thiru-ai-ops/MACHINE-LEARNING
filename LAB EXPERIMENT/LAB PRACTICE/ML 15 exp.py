temp = []

for i in range(7):
    temp.append(float(input("Enter temperature: ")))

print("Maximum =", max(temp))
print("Minimum =", min(temp))
print("Average =", sum(temp) / 7)
