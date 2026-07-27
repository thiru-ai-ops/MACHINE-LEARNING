p = input("Enter password: ")

if (len(p) >= 8 and any(c.isupper() for c in p) and
    any(c.islower() for c in p) and
    any(c.isdigit() for c in p) and
    any(not c.isalnum() for c in p)):
    print("Valid Password")
else:
    print("Invalid Password")
