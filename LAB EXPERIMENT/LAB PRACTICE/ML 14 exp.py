total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percent = (attended / total) * 100

print("Attendance =", round(percent, 2), "%")

if percent >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")
