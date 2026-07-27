w = float(input("Enter weight (kg): "))
h = float(input("Enter height (m): "))

bmi = w / (h * h)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
else:
    status = "Obese"

print("BMI =", round(bmi, 2))
print("Health Status =", status)
