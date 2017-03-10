numberOfItems = int(input("Number of items: "))

while numberOfItems < 0:
    print("that is not a valid number of items")
    numberOfItems = input(print("Number of items: "))

totalPrice = 0
for i in range(1, numberOfItems + 1):
    priceOfItem = int(input("Price of item: "))
    totalPrice += priceOfItem

if totalPrice > 100:
    totalPrice *= 0.9
print("Total price for", numberOfItems, "items is ${:.2f}".format(totalPrice))

