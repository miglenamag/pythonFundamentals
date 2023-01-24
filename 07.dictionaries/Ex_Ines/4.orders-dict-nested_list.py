products = {}
data = input()
while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = [price, quantity]
    else:
        products[product][0] = price
        products[product][1] += quantity
    data = input()

for product in products:
    total_price = products[product][0] * products[product][1]
    print(f" {product} ->{total_price:.2f}")