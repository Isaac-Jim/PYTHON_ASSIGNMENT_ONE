

# 1. Store items and prices in a dictionary
prices = {
    "Bread": 25,
    "Milk": 18,
    "Eggs": 2.5,
    "Sugar": 20
}

# Dictionary to store how many items the user buys
quantities = {}

# 2. Ask user for quantities using a loop
for item, price in prices.items():        # using .items() dictionary method
    quantity = int(input(f"How many {item} do you want to buy? "))
    quantities[item] = quantity                # store the quantity

# 3. Compute cost
subtotal = 0

for item in prices:
    subtotal += prices[item] * quantities[item]

# Apply discount if subtotal > 100
if subtotal > 100:
    discount = 0.10 * subtotal
else:
    discount = 0

total = subtotal - discount

# 4. Print receipt
print("\n----- RECEIPT ------")

for item in prices:
    item_total = prices[item] * quantities[item]
    print(f"{item} (x{quantities[item]}): GHS {item_total:.2f}")

print("-------------------")
print(f"Subtotal: GHS {subtotal:.2f}")
print(f"Discount: GHS {discount:.2f}")
print(f"Total: GHS {total:.2f}")
