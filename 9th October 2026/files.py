# file = open("employees.txt", "w")
#
# file.write("101,Aman,IT,75000\n")
# file.write("102,Meera,HR,65000\n")
# file.write("103,Rohan,Finance,70000\n")
#
# file.close()

#
# file = open("employees.txt", "r")
#
# data = file.read()
#
# print(data)
#
# file.close()

# file = open("employees.txt", "r")
#
# for line in file:
#     print(line.strip())
#
# file.close()
#
# file = open("employees.txt", "a")
# file.write("104, Sara, Sales, 68000\n")
# file.close()

#Unstructured Data -- Text, Audio, Video, PDF, Doc -- Azure Cloud

# Semi Structured Data -- JSON -- Mongo DB

# Structure Data -- Tables --- MY SQL
#
# import csv  #comma separated values
#
# with open("products.csv", "w", newline="") as file:
#
#     writer = csv.writer(file)
#
#     writer.writerow([
#         "product_id",
#         "product_name",
#         "category",
#         "price"
#     ])
#
#     writer.writerow([101, "Laptop", "Electronics", 65000])
#     writer.writerow([102, "Mouse", "Accessories", 1500])
#     writer.writerow([103, "Office Chair", "Furniture", 9000])
#     writer.writerow([104, "Monitor", "Electronics", 18000])

# import csv
# with open("products.csv","r") as  file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# 
# import csv
# with open("products.csv","r") as file:
#     reader=csv.DictReader(file)
#     for row in reader:
#         print(row)