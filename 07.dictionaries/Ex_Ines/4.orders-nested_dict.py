products = {}
data = input()
while not data == "buy":
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = {"price":price, "quantity":quantity}
    else:
        products[product]["price"] = price
        products[product]["quantity"] += quantity
    data = input()
    
for product in products:
    total_price = products[product]["price"]* products[product]["quantity"]
    print(f" {product} ->{total_price:.2f}")