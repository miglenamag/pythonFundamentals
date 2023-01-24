products_price = {}
products_quantity = {}
data = input()
while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if product not in products_price:
        products_price[product] = price
        products_quantity[product] = quantity
    else:
        products_price[product] = price
        products_quantity[product] += quantity
    data = input()

# for product, price in products_price.items():
#     total_price = products_price[product]*products_quantity[product]
#     print (f"{product} -> {total_price:.2f}")

for product in products_price:
    total_price = products_price[product]*products_quantity[product]
    print (f"{product} -> {total_price:.2f}")





