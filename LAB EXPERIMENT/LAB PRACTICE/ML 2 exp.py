basic = float(input())
hra = float(input())
da = float(input())

gross = basic + hra + da
pf = gross * 0.12
tax = gross * 0.10
net = gross - pf - tax

print("Gross Salary =", gross)
print("PF =", pf)
print("Tax =", tax)
print("Net Salary =", net)
