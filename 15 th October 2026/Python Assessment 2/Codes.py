#Assessment 2 — Logistics & Employee Data Processing
#Python Fundamentals
# weight=float(input("Enter your weight: "))
# cost=float(input("Enter your cost: "))
#
# if weight > 0:
#     cost_per_kg = cost / weight
#     print(f"Cost per kg: {cost_per_kg:.2f}")
# else:
#     print("Weight must be greater than zero")
#
# if weight>20:
#     print("Heavy")
# elif weight>=10 and weight<=20:
#     print("Medium")
# elif weight<10:
#     print("Light")
# else:
#     print("Weight must be greater than 0")
#
# for i in range(1,21):
#     print(i)
#
# for i in range(1,21):
#     if i%2==0:
#         print(i)
# i=1
# while(i<6):
#     print("Processing attempt ",i)
#     i=i+1
import json


# #Collections
# costs=[850, 620, 1250, 480,1600, 740, 590, 1100,920, 1750, 520, 1050]
#
# print("Total:", sum(costs))
# print("Average:", sum(costs) / len(costs))
# print("Minimum:", min(costs))
# print("Maximum:", max(costs))
#
#
# destinations = [
#     "Hyderabad", "Mumbai", "Bangalore",
#     "Delhi", "Pune", "Hyderabad",
#     "Mumbai", "Delhi", "Bangalore",
#     "Pune", "Hyderabad", "Mumbai"
# ]
# unique_destinations = set(destinations)
# print(unique_destinations)
#
#
# shipment = {
#     "shipment_id": "S1001",
#     "destination": "Hyderabad",
#     "weight": 12.5,
#     "status": "Delivered",
#     "cost": 850
# }
# print(shipment)
#
#
# shipments = [
#     {
#         "shipment_id": "S1001",
#         "destination": "Hyderabad",
#         "status": "Delivered",
#         "cost": 850
#     },
#     {
#         "shipment_id": "S1002",
#         "destination": "Mumbai",
#         "status": "In Transit",
#         "cost": 620
#     },
#     {
#         "shipment_id": "S1003",
#         "destination": "Bangalore",
#         "status": "Delivered",
#         "cost": 1250
#     },
#     {
#         "shipment_id": "S1004",
#         "destination": "Delhi",
#         "status": "Pending",
#         "cost": 480
#     }
# ]
#
#
# delivered_shipments = []
# for shipment in shipments:
#     if shipment["status"]=="Delivered":
#         delivered_shipments.append(shipment)
# print(delivered_shipments)
#
#Functions/Lambda
#
# def calculate_shipping_cost(weight, rate_per_kg):
#     return weight * rate_per_kg
#
# print(calculate_shipping_cost(12.5, 68))
#
# def shipment_category(weight):
#     if weight > 20:
#         return "Heavy"
#     elif weight >= 10:
#         return "Medium"
#     else:
#         return "Light"
#
# print(shipment_category(18.5))
#
# shipments = [
#     {"id": "S1001", "destination": "Hyderabad",
#      "status": "Delivered", "cost": 850},
#
#     {"id": "S1002", "destination": "Mumbai",
#      "status": "In Transit", "cost": 620},
#
#     {"id": "S1003", "destination": "Bangalore",
#      "status": "Delivered", "cost": 1250}
# ]
# delivered=list(filter(lambda x:x["status"]=="Delivered",shipments))
# print(delivered)
# destinations=list(map(lambda x:x["destination"],delivered))
# print(destinations)
# sorted_shipments=sorted(shipments,key=lambda x:x["cost"],reverse=True)
# print(sorted_shipments)
#
# #OOP
# class Shipment:
#     def __init__(self,shipment_id,destination,weight,cost):
#         self.id = shipment_id
#         self.destination = destination
#         self.weight = weight
#         self.cost = cost
#     def display(self):
#         print(self.id)
#         print(self.destination)
#         print(self.weight)
#         print(self.cost)
# class ExpressShipment(Shipment):
#     def __init__(self,shipment_id,destination,weight,cost,surcharge):
#         super().__init__(shipment_id,destination,weight,cost)
#         self.surcharge = surcharge
#     def display(self):
#         print(self.id)
#         print(self.destination)
#         print(self.weight)
#         print(self.cost)
#         print(self.surcharge)
# s1=Shipment("S1001","Hyderabad",80,100)
# s2=ExpressShipment("S1002","Hyderabad",80,100,20)
# l=[s1,s2]
# for shipment in l:
#     shipment.display()
#
# #JSON
#
# with open("employees.json","r") as f:
#     employees = json.load(f)
#     for employee in employees:
#         print(employee["name"])
# print("--------------")
# for employee in employees:
#     if(employee["salary"]>75000):
#         print(employee["name"])
# print("--------------")
# for employee in employees:
#     if("Python" in employee["skills"]):
#         print(employee["name"])
# print("--------------")
# for employee in employees:
#     print(employee["name"],employee["performance"]["rating"])
# print("--------------")
# for employee in employees:
#     if(employee["performance"]["rating"]>4.5):
#         print(employee["name"])
# sorted_employees=sorted(employees,key=lambda x:x["performance"]["rating"],reverse=True)
# print(sorted_employees)
# for employee in employees:
#     if employee["employee_id"] == 303:
#         employee["skills"].append("Pandas")
# with open("employees_updated.json","w") as file:
#     json.dump(employees,file,indent=4)
# print("Updated employee JSON created successfully")

#Modules
#in shipment_utils.py and main.py

#Pandas

import pandas as pd
#
shipments_df = pd.read_csv("shipments.csv")
# print(shipments_df)
#
# delivered_shipments = shipments_df[
#     shipments_df["status"] == "Delivered"
# ]
# print(delivered_shipments)
#
# status_count = shipments_df["status"].value_counts()
# print(status_count)
#
# shipments_df["shipment_date"] = pd.to_datetime(
#     shipments_df["shipment_date"]
# )
# print(shipments_df.dtypes)
#
# shipments_df["month"] = shipments_df["shipment_date"].dt.month
#
# monthly_status = shipments_df.groupby(
#     ["month", "status"]
# ).size().reset_index(name="shipment_count")
#
# print(monthly_status)
#
# average_cost = shipments_df.groupby(
#     "destination"
# )["cost"].mean()
# print(average_cost)
#
# total_weight = shipments_df.groupby(
#     "destination"
# )["weight"].sum()
# print(total_weight)
#
# selected_columns = [
#     "shipment_id",
#     "destination",
#     "weight",
#     "status",
#     "cost"
# ]
# selected_df = pd.read_csv(
#     "shipments.csv",
#     usecols=selected_columns
# )
# print(selected_df)
#
#
hubs_df = pd.read_csv("hubs.csv")
# print(hubs_df)
#
joined_df = pd.merge(
    shipments_df,
    hubs_df,
    on="hub_id",
    how="inner"
)
# print(joined_df)
#
# hub_cost = joined_df.groupby(
#     ["hub_id", "hub_name"]
# )["cost"].sum().reset_index(name="total_cost")
# print(hub_cost)
#
# hub_count = joined_df.groupby(
#     ["hub_id", "hub_name"]
# )["shipment_id"].count().reset_index(name="total_shipments")
#
# print(hub_count)
#
# hub_summary = joined_df.groupby(
#     ["hub_id", "hub_name"]
# ).agg(
#     total_shipments=("shipment_id", "count"),
#     total_cost=("cost", "sum")
# ).reset_index()
#
# hub_summary = hub_summary.sort_values(
#     by="total_cost",
#     ascending=False
# )
# print(hub_summary)
#
# hub_summary.to_csv(
#     "hub_summary.csv",
#     index=False
# )
#
# hub_summary.to_json(
#     "hub_summary.json",
#     orient="records",
#     indent=4
# )
# print("Hub summary files created successfully")
#
#Pandas/NumPy Enrichment
import pandas as pd
import numpy as np

joined_df["cost_per_kg"] = (
    joined_df["cost"] / joined_df["weight"]
)

print(
    joined_df[
        ["shipment_id", "cost", "weight", "cost_per_kg"]
    ]
)


joined_df["cost_category"] = np.where(
    joined_df["cost"] >= 1200,
    "Expensive",
    "Normal"
)

print(
    joined_df[
        ["shipment_id", "cost", "cost_category"]
    ]
)

conditions = [
    (joined_df["status"] == "Delivered") &
    (joined_df["cost"] < 1200),

    (joined_df["status"] == "Delivered") &
    (joined_df["cost"] >= 1200),

    joined_df["status"] == "In Transit",

    joined_df["status"] == "Pending"
]

categories = [
    "Efficient",
    "Delivered - High Cost",
    "In Progress",
    "Needs Attention"
]

joined_df["performance_category"] = np.select(
    conditions,
    categories,
    default="Unknown"
)

print(
    joined_df[
        [
            "shipment_id",
            "status",
            "cost",
            "performance_category"
        ]
    ]
)


joined_df.to_csv(
    "shipment_analysis.csv",
    index=False
)

print("Shipment analysis file created successfully")

