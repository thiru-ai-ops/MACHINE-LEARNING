stock = int(input("Enter available stock: "))
min_stock = int(input("Enter minimum stock: "))

if stock < min_stock:
    print("Low Stock! Reorder Required")
else:
    print("Stock Available")
