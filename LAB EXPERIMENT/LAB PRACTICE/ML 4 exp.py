balance = 10000
pin = 1234

p = int(input("Enter PIN: "))

if p == pin:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance =", balance)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")
