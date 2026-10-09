import json
#upload or create
products = [
    {
        "product_id": 101,
        "product_name": "Laptop",
        "category": "Electronics",
        "price": 65000
    },
    {
        "product_id": 102,
        "product_name": "Mouse",
        "category": "Accessories",
        "price": 1500
    },
    {
        "product_id": 103,
        "product_name": "Monitor",
        "category": "Electronics",
        "price": 18000
    }
]

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)

#read
import json
with open("products.json","r") as file:
    products = json.load(file)
print(products)

#modify
import json
with open('products.json','r') as file:
    products = json.load(file)
for product in products:
    if product["product_id"]==101:
        product["price"]=70000
with open('products.json','w') as file:
    json.dump(products,file,indent=4)