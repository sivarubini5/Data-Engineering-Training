
#question link https://drive.google.com/file/d/1_puQ9zvnG0qfs3wBIOjPOCDoey80EUVd/view
#Exercise Set 1 — CSV, Lists, Lambda, Filter, Map, Set,Sorting

# Create a file named:shipments.csv
#
# with:
#
# shipment_id,customer,city,weight,status,cost
# S101,Alpha Stores,Hyderabad,12.5,Delivered,850
# S102,Metro Mart,Mumbai,8.2,In Transit,620
# S103,Fresh Foods,Hyderabad,15.0,Delivered,1100
# S104,Quick Shop,Pune,5.5,Pending,450
# S105,Urban Retail,Mumbai,20.0,Delivered,1450
# S106,Daily Needs,Delhi,9.8,In Transit,700
# S107,Smart Bazaar,Hyderabad,7.5,Pending,550
# S108,Green Market,Delhi,18.2,Delivered,1300
#
# Tasks
#
# 1. Read shipments.csv using Python's csv module.
# 2. Store all records inside a Python list.
# 3. Display the complete list.
# 4. Display only:
# shipment ID
# customer
# status
# 5. Convert weight and cost from strings to numeric values.
# 6. Calculate the total shipping cost.
# 7. Find shipments whose cost is greater than 700 .
# 8. Use filter() and lambda to display only Delivered shipments.
# 9. Use filter() and lambda to find shipments weighing more than 10 .
# 10. Use map() to extract all city names.
# 11. Use map() + set() to get the unique cities.
# 12. Sort the shipment list by cost from lowest to highest using key .
#
# 13. Sort by weight from highest to lowest.
# 14. Sort alphabetically by customer name.
# 15. Create a lambda function that calculates:
#
# cost per kg = cost / weight
#
# and display it for every shipment.

import csv
with open("shipments.csv","r") as file:
    reader=csv.DictReader(file)
    list_val=list(reader)
print("all_values")
print(list_val)
print("shipment_id,customer,status")
for i in list_val:
    print(i["shipment_id"],i["customer"],i["status"])
for i in list_val:
    i["weight"]=float(i["weight"])
    i["cost"]=float(i["cost"])
print("Float cost and weight")
print(list_val)
print("sum of cost:")
print(sum(map(lambda x:x["cost"],list_val)))
print("Cost >700:")
for i in list_val:
    if i["cost"]>700:
        print(i)

filtered=list(filter(lambda x:x["status"]=="Delivered",list_val))
print("Delivered:")
print(filtered)

filtered=list(filter(lambda x:x["weight"]>10,list_val))
print("Weight >10:")
print((filtered))

cities=list(map(lambda x:x["city"],list_val))
print("Cities:")
print(cities)

cities=set(map(lambda x:x["city"],list_val))
print("Unique Cities:")
print(cities)

sorted_val=sorted(list_val,key=lambda x:x["cost"])
print("cost in ascending order:")
for i in sorted_val:
    print(i["shipment_id"],i["cost"])

sorted_val_by_weight=sorted(list_val,key=lambda x:x["weight"],reverse=True)
print("weight in descending order:")
for i in sorted_val_by_weight:
    print(i["shipment_id"],i["weight"])

sorted_val_by_name=sorted(list_val,key=lambda x:x["customer"])
print("name in ascending order:")
for i in sorted_val_by_name:
    print(i["customer"])

cost_per_kg=lambda x:x["cost"]/x["weight"]
for i in list_val:
    print(i["shipment_id"],round(cost_per_kg(i),2))
# Exercise Set 2 — Lists and Tuples
#
# Use:
#
# sales = [
# ("North", 12000),
# ("South", 18000),
# ("West", 9500),
# ("North", 22000),
# ("East", 15000),
# ("South", 11000)
# ]
#
# Tasks
#
# 1. Display all tuples.
# 2. Display only the region from every tuple.
# 3. Display only the sales amount.
# 4. Find sales greater than 12000 .
# 5. Calculate total sales.
# 6. Find the highest and lowest sales amount.
# 7. Create a list containing only sales amounts.
# 8. Find unique regions using a set.
# 9. Sort the tuples based on sales amount.
# 10. Sort the tuples based on region name.
#


sales = [
("North", 12000),
("South", 18000),
("West", 9500),
("North", 22000),
("East", 15000),
("South", 11000)
]
print("All")
print(sales)

for i in sales:
    print(i[0])

for i in sales:
    print(i[1])

for i in sales:
    if i[1]>12000:
        print(i)

print("total sales")
print(sum(item[1] for item in sales))

amounts=[i[1] for i in sales]

print("max:",max(amounts))
print("min:",min(amounts))

print(amounts)

print("Unique regions:")
print(set(i[0] for i in sales))

print("Sort by sales amount")
print(sorted(sales,key=lambda x:x[1]))

print("Sort by name")
print(sorted(sales,key=lambda x:x[0]))

# Exercise Set 3 — JSON Processing
#
# Create:
#
# projects.json
#
# with:
#
# [
# {
# "project_id": 101,
# "project_name": "Data Migration",
# "department": "IT",
# "budget": 450000,
# "technologies": ["Python", "SQL", "Azure"],
# "team": [
# {
# "name": "Vikram",
# "role": "Engineer",
# "experience": 4
# },
# {
# "name": "Meera",
# "role": "Analyst",
# "experience": 3
# }
# ]
# },
# {
# "project_id": 102,
# "project_name": "Customer Analytics",
# "department": "Analytics",
# "budget": 300000,
# "technologies": ["Python", "Pandas", "Power BI"],
# "team": [
# {
# "name": "Karan",
# "role": "Data Analyst",
# "experience": 5
# },
# {
# "name": "Zoya",
# "role": "Developer",
# "experience": 2
# }
#
# ]
# },
# {
# "project_id": 103,
# "project_name": "Cloud Modernization",
# "department": "Cloud",
# "budget": 600000,
# "technologies": ["Azure", "Docker", "Python"],
# "team": [
# {
# "name": "Naveen",
# "role": "Cloud Engineer",
# "experience": 6
# },
# {
# "name": "Isha",
# "role": "Engineer",
# "experience": 4
# }
# ]
# }
# ]

# Tasks
#
# 1. Read the JSON file into Python.
# 2. Check the datatype of the returned object.
# 3. Display all project names.
# 4. Display projects having a budget above ₹4,00,000 .
# 5. Display projects that use Python .
# 6. Calculate the total budget of all projects.
# 7. Extract all technologies into one Python list.
# 8. Find the unique technologies.
# 9. Display every team member's:
# name
# role
# experience
# 10. Display team members having more than 3 years of experience.
# 11. Find the total number of team members across all projects.
# 12. Sort projects by budget from highest to lowest.
# 13. Sort projects alphabetically by project name.
# 14. Sort each project's team members based on experience.

import json
with open("projects.json","r") as file:
    projects=json.load(file)
print("loaded")

print("datatype: ",type(projects))

print("project names")
for i in projects:
    print(i["project_name"])

print("budget>4lakh")
for i in projects:
    if i["budget"]>400000:
        print(i)

print("projects using Python")
for i in projects:
    if "Python" in i["technologies"]:
        print(i["project_name"])

print("total budget")
print(sum(map(lambda x:x["budget"],projects)))

all_tech=[]

for i in projects:
    all_tech.extend(i["technologies"])
print("all tech")
print(all_tech)

unique_tech=set(all_tech)
print(unique_tech)

print("Team member details:")
for i in projects:
    for j in i["team"]:
        print("Name: ",j["name"]," Role: ",j["role"]," Experience: ",j["experience"])

print("Team members with experience > 3 years:")
for i in projects:
    fil_list=filter(lambda x:x["experience"]>3,i["team"])
    for j in fil_list:
        print(j["name"],j["experience"])

print("No of members")
print(sum(len(i["team"]) for i in projects))

sorted_by_budget=sorted(projects,key=lambda x:x["budget"],reverse=True)
for i in sorted_by_budget:
    print(i["project_name"],i["budget"])

sorted_by_name = sorted(projects, key=lambda x: x["project_name"])
for i in sorted_by_name:
    print(i["project_name"], i["budget"])

for project in projects:
    s=sorted(project["team"],key=lambda x:x["experience"])
    print("Project: ",project["project_name"])
    for j in s:
        print(j["name"],j["experience"])