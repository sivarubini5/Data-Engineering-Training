# class Product:
#     name="Laptop"
#     price=1600
# p1=Product()#Create an object -- Product prod = new Product() in other languages but no new keywordin python
# print(p1.name)
# print(p1.price)
#
# #dynamic
# class Product1:
#     name=""
#     price=0
# p2=Product1()
# p2.name="Laptop"
# p2.price=6500
#
# p3=Product1()
# p3.name="Mouse"
# p3.price=1500
#
# print(p2.name,p2.price)
# print(p3.name,p3.price)
#
#
# class Product:
#     name=""
#     price=0
#     def display(self):
#         print(f"Product: {self.name}")
#         print(f"Price: {self.price}")
# p1=Product()
# p1.name="Monitor"
# p1.price=18000
# p1.display()

#self is like this in java if we need to use that we need to pass as parameters
#public variables can be accessed anywhere
# class Product():
#     name=""
#     price=0
#     quantity=0
#     def total_amount(self):
#         return self.price*self.quantity
# p1=Product()
# p1.name="Laptop"
# p1.price=6500
# p1.quantity=2
# print(p1.total_amount())

#protected can be accessed within the file
#
# class Employee:
#     _department="IT"
# e1 = Employee()
# print(e1._department)

# #private
# class Employee:
#     __bonus=1000
# e1=Employee()
# print(e1.__bonus)

#constructor
# class Product:
#     def __init__(self):
#         print("Product object created")
# p1=Product()

#Parameterized constructor
# class Employee:
#     def __init__(self,emp_id,name,department,salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.department = department
#         self.salary = salary
# e1=Employee(101,"Aman","IT",75000)
# e2=Employee(102,"Sara","HR",65000)
