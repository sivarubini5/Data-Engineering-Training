# drive link https://drive.google.com/drive/folders/1p4SiF-0_OzuKrP1Lyxe4503edxNURNQ3
from os import lstat  ## Section A — Python Basics

prod_name=input("enter product name: ")
unit_price=int(input("enter unit price: "))
quantity=int(input("enter quantity: "))

total_amount=unit_price*quantity
print(f"{prod_name} total is {total_amount}")

discount=0
disc_percent=0
if(total_amount>=50000):
    disc_percent=10
    discount=total_amount-(total_amount*0.1)
else:
    disc_percent=5
    discount=total_amount-(total_amount*0.05)

print(f"{prod_name} original amount is {total_amount}.After {disc_percent} % discount finalamount is {discount}.")

stock_quantity=int(input("enter stock quantity: "))
if(stock_quantity>20):
    print("High Stock")
elif(stock_quantity<=20 and stock_quantity>=1):
    print("Low Stock")
elif(stock_quantity<=0):
    print("Out Of Stock")

for i in range(1,10):
    print(i,end=" ")
print()
stock=5
while(stock>0):
    print(stock,end=" ")
    stock-=1
print()
for i in range(1,10):
    if i==5:
        continue
    elif i==8:
        break
    else:
        print(i,end=" ")

#Section B — Lists, Tuples, Sets and Dictionaries
sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]
print("Sum",sum(map(lambda x: x, sales)))

print("Max",max(map(lambda x: x, sales)))
print("Min",min(map(lambda x: x, sales)))

print("Greter than 20000")
for i in sales:
    if(i>20000):
        print(i)

sor=sorted(sales,reverse=True)
print("Sorted : ",sor)

cities = [
"Hyderabad",
"Mumbai",
"Delhi",
"Hyderabad",
"Pune",
"Mumbai"
]
unique=set(cities)
print("Unique cities: ",unique)

product_info = ("P10023", "Wireless Headphones", "Electronics", 89.99)
product_id, product_name, category, price = product_info
print("Product ID : ",product_id)
print("Product Name : ",product_name)
print("Category : ",category)
print("Price : ",price)

dic={
    "id":101,
    "name":"Abi",
    "city":"Coimbatore",
    'Orders':3,
    "ActiveStatus":True
}
print(f"Customer:{dic["name"]} ,ID:{dic["id"]} ,City:{dic["city"]}")

dic["city"]="Chennai"
print("After changing city")
print(f"Customer:{dic["name"]} ,ID:{dic["id"]} ,City:{dic["city"]}")

dic["Orders"]=dic["Orders"]+1
print("After increasing order count")
print(f"Orders:{dic["Orders"]}")

dic["Email"]="abi@gmail.com"
print("Added mail")
print(dic["Email"])

for k in dic.items():
    print(k)

#Section C — Functions and Lambda
def calculate_total(price, quantity):
    return  price*quantity
print(calculate_total(65000, 2))

def calculate_discount(amount):
    discount=0
    disc_percent=0
    if(amount>=50000):
        disc_percent=10
        discount=amount-(amount*0.1)
    else:
        disc_percent=5
        discount=amount-(amount*0.05)
    return (f"original amount is {amount}.After {disc_percent} % discount finalamount is {discount}.")
print(calculate_discount(65000))

def total_sales(sales):
    return sum(sales)
sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]
print(total_sales(sales))

def check_stock(products):
    if(products['stock']>0):
        return ("Available")
    else:
        return ("Out of stock")
product = {
    "product_name": "Laptop",
    "stock": 12
}
print(check_stock(product))

sq=lambda x:x**2
print(sq(5))

f=list(filter(lambda x:x>20000,sales))
print(f)

customers = [
    {"name": "North Star Retail", "city": "Hyderabad"},
    {"name": "Blue Mart", "city": "Mumbai"},
    {"name": "Prime Stores", "city": "Hyderabad"},
    {"name": "Fresh Point", "city": "Delhi"}
]
cities=(list(map(lambda x:x["city"],customers)))
print(cities)

uni=set(cities)
print(uni)

products = [
    {"name": "Laptop", "price": 65000},
    {"name": "Monitor", "price": 18000},
    {"name": "Keyboard", "price": 3000}
]
print(sorted(products,key=lambda x:x["price"]))

#Section D — OOP
class Product:
    def __init__(self, product_id,product_name, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock = stock
    def display_product(self):
        print(f"{self.product_id} {self.product_name} {self.price} {self.stock}")
    def calculate_value(self):
        return (self.price*self.stock)

p1 = Product(201, "Laptop", 65000, 12)
p2 = Product(202, "Monitor", 18000, 8)

p1.display_product()
print("Inventory Value:", p1.calculate_value())

p2.display_product()
print("Inventory Value:", p2.calculate_value())

class DiscountedProduct(Product):
    def __init__(self, product_id, product_name, price,
                 stock, discount_percent):
        super().__init__(product_id, product_name, price, stock)

        self.discount_percent = discount_percent

    def display_product(self):
        super().display_product()
        print("Discount:", self.discount_percent, "%")
p3 = DiscountedProduct(203, "Office Chair", 9000, 15, 10)

p3.display_product()

class PremiumProduct(Product):
    def display_product(self):
        print("Premium Product Details")
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Stock:", self.stock)

p4 = PremiumProduct(204, "Keyboard", 3000, 30)

product_list = [p1, p2, p3, p4]

for product in product_list:
    print("--------------------")
    product.display_product()

#Section E — Text, CSV and JSON Files
with open("activity.txt","w") as file:
    file.write("Processing started\n")
    file.write("Customer data loaded\n")
    file.write("Order data processed\n")
with open("activity.txt","a") as file:
    file.write("Processing completed\n")
with open("activity.txt","r") as file:
    content = file.read()
    print(content)

import csv
with open("customers.csv","r",newline="") as file:
    reader = csv.DictReader(file)
    records=list(reader)
print("Active customer:")
for i in records:
    if(i["active"]==True):
        print(i)
print("Hyderabad customers:")
for i in records:
    if(i["city"]=="Hyderabad"):
        print(i)

import json
with open("products.json","r") as file:
    customer = json.load(file)
print("All products:")
for i in customer:
    print(i["product_name"])
for i in customer:
    if(i["price"]>10000):
        print(i["product_name"],i["price"])
for i in customer:
    print(i["supplier"]["name"],i["supplier"]["city"])
colors=[]
for i in customer:
    colors.extend(i["colors"])
print(colors)
print("Unique colors: ",set(colors))
for i in customer:
    if(i["product_id"]==202):
        i["stock"]=i["stock"]+1
with open("products_updated.json","w") as file:
    json.dump(customer,file,indent=4)
print("Updated json file created successfully")
