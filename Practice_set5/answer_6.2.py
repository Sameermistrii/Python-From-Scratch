products = {
    "apple": 50,
    "banana": 30,
    "mango": 80
}

highest_price = 0
highest_product = ""

for product, price in products.items():
    if price > highest_price:
        highest_price = price
        highest_product = product

print(highest_product)
print(highest_price)

# this one is also correct but not the best way to do it

products = {
    "Bag": 420,
    "Drink": 120,
    "Pen": 10,
    "Phone": 19978,
    "Laptop": 49878
}

replace = list(products.values())
replace.sort()

highest_price = replace[-1]

for product, price in products.items():
    if price == highest_price:
        print(product, price)