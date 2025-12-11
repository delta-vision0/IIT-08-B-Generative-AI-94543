# Reading the CSV file
file = open("products.csv", "r")
lines = file.readlines()
file.close()

# Removing header
header = lines[0]
data = lines[1:]

print("---- Product Details ----")
for line in data:
    pid, name, cat, price, qty = line.strip().split(",")
    print(f"ID: {pid}, Name: {name}, Category: {cat}, Price: {price}, Qty: {qty}")

# Total rows
total_rows = len(data)
print("\nTotal rows:", total_rows)

# Products priced above 500
count_above_500 = 0
for line in data:
    price = int(line.strip().split(",")[3])
    if price > 500:
        count_above_500 += 1
print("Products above 500:", count_above_500)

# Average price
total_price = 0
for line in data:
    price = int(line.strip().split(",")[3])
    total_price += price
avg_price = total_price / total_rows
print("Average price:", avg_price)

# Products by category
user_cat = input("\nEnter category name: ")
print(f"Products in category '{user_cat}':")
found = False
for line in data:
    pid, name, cat, price, qty = line.strip().split(",")
    if cat.lower() == user_cat.lower():
        print("-", name)
        found = True
if not found:
    print("No products found.")

# Total quantity
total_qty = 0
for line in data:
    qty = int(line.strip().split(",")[4])
    total_qty += qty
print("\nTotal quantity in stock:", total_qty)
