#Section A — Python Basics
attendee_name = input("Enter attendee name: ")
tickets = int(input("Enter number of tickets: "))
ticket_price = float(input("Enter ticket price: "))

total_amount = tickets * ticket_price

if total_amount >= 10000:
    discount = total_amount * 0.10
else:
    discount = total_amount * 0.05

final_amount = total_amount - discount

print(f"Attendee Name: {attendee_name}")
print(f"Tickets: {tickets}")
print(f"Original Amount: {total_amount:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Amount: {final_amount:.2f}")


capacity = int(input("Enter event capacity: "))
registered = int(input("Enter registered participants: "))

if capacity < 0 or registered < 0:
    print("Invalid Data")
elif registered == capacity:
    print("Full")
elif registered < capacity:
    print("Seats Available")
else:
    print("Invalid Data")

for i in range(1, 16):
    print(i)

for i in range(1, 16):
    if i % 3 == 0:
        print(i)

count = 10

while count >= 1:
    print(count)
    count -= 1

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

for i in range(1, 11):
    if i == 8:
        break
    print(i)

#Section B — Lists, Tuples, Sets and Dictionaries
booking_amounts = [
5000, 3500, 7500, 6000,
4000, 7000, 3000, 10000]

print("Total:", sum(booking_amounts))


average = sum(booking_amounts) / len(booking_amounts)
print("Average:", average)

print("Highest:", max(booking_amounts))
print("Lowest:", min(booking_amounts))

for amount in booking_amounts:
    if amount > 5000:
        print(amount)

sorted_amounts = sorted(booking_amounts, reverse=True)
print(sorted_amounts)


cities = [
    "Hyderabad",
    "Mumbai",
    "Pune",
    "Hyderabad",
    "Delhi",
    "Mumbai"
]

unique_cities = set(cities)
print(unique_cities)

unique_cities.add("Chennai")
print(unique_cities)

print(len(unique_cities))

event = (
    "E101",
    "AI Innovation Summit",
    "Hyderabad",
    500
)

event_id, event_name, venue, capacity = event
print(event_id)
print(event_name)
print(venue)
print(capacity)

registration = {
    "registration_id": "R1001",
    "attendee_name": "Aarav Shah",
    "city": "Hyderabad",
    "tickets": 2,
    "status": "Confirmed",
    "amount": 5000
}

registration["status"] = "Pending"

registration["tickets"] += 1

registration["email"] = "aarav@example.com"

for key, value in registration.items():
    print(key, ":", value)

#Section C — Functions, Lambda, Filter, Map
def calculate_booking(ticket_price, tickets):
    return ticket_price * tickets
print(calculate_booking(2500, 2))

def calculate_discount(amount):
    if amount >= 10000:
        return amount * 0.10
    else:
        return amount * 0.05
print(calculate_discount(12000))

def is_active(status):
    return status == "Confirmed"
print(is_active("Confirmed"))

def total_booking(amounts):
    return sum(amounts)
booking_amounts = [
    5000, 3500, 7500, 6000,
    4000, 7000, 3000, 10000
]
print(total_booking(booking_amounts))

increase_amount = lambda amount: amount * 1.10
print(increase_amount(5000))

filtered_amounts = list(
    filter(lambda x: x > 6000, booking_amounts)
)
print(filtered_amounts)

registrations = [
    {
        "name": "Aarav Shah",
        "city": "Hyderabad",
        "status": "Confirmed",
        "amount": 5000
    },
    {
        "name": "Simran Kaur",
        "city": "Mumbai",
        "status": "Confirmed",
        "amount": 3500
    },
    {
        "name": "Faiz Ahmed",
        "city": "Pune",
        "status": "Pending",
        "amount": 7500
    },
    {
        "name": "Keerthi Rao",
        "city": "Bangalore",
        "status": "Confirmed",
        "amount": 6000
    }
]
confirmed = list(
    filter(
        lambda x: x["status"] == "Confirmed",
        registrations
    )
)
print(confirmed)

attendee_cities = list(
    map(lambda x: x["city"], registrations)
)
print(attendee_cities)

unique_cities = set(
    map(lambda x: x["city"], registrations)
)
print(unique_cities)

sorted_registrations = sorted(
    registrations,
    key=lambda x: x["amount"]
)
print(sorted_registrations)

#Section D — OOP
class Event:

    def __init__(self, event_id, event_name,
                 capacity, ticket_price):

        self.event_id = event_id
        self.event_name = event_name
        self.capacity = capacity
        self.ticket_price = ticket_price

    def display_event(self):
        print("Event ID:", self.event_id)
        print("Event Name:", self.event_name)
        print("Capacity:", self.capacity)
        print("Ticket Price:", self.ticket_price)

    def calculate_revenue(self, tickets_sold):
        return tickets_sold * self.ticket_price

e1 = Event("E101", "AI Innovation Summit", 500, 2500)
e2 = Event("E102", "Leadership Forum", 350, 3500)
e1.display_event()
print("Revenue:", e1.calculate_revenue(100))
e2.display_event()
print("Revenue:", e2.calculate_revenue(50))

class OnlineEvent(Event):
    def __init__(self, event_id, event_name,
                 capacity, ticket_price, platform):
        super().__init__(
            event_id, event_name, capacity, ticket_price
        )
        self.platform = platform
    def display_event(self):
        super().display_event()
        print("Platform:", self.platform)

class PhysicalEvent(Event):
    def __init__(self, event_id, event_name,
                 capacity, ticket_price, venue):
        super().__init__(
            event_id, event_name, capacity, ticket_price
        )
        self.venue = venue
    def display_event(self):
        super().display_event()
        print("Venue:", self.venue)

online = OnlineEvent(
    "E106", "Python Webinar", 1000, 500, "Zoom"
)
physical = PhysicalEvent(
    "E107", "Tech Conference", 300, 2000, "Hyderabad"
)
event_list = [online, physical]
for event in event_list:
    print("--------------------")
    event.display_event()

#Section E — Text File Handling

with open("event_log.txt", "w") as file:
    file.write("Event processing started\n")
    file.write("Registration data loaded\n")
    file.write("Registration validation completed\n")
with open("event_log.txt", "a") as file:
    file.write("Event report generated\n")
    file.write("Event processing completed\n")
with open("event_log.txt", "r") as file:
    content = file.read()
    print(content)
with open("event_log.txt", "r") as file:
    for line in file:
        print(line)
with open("event_log.txt", "r") as file:
    for line in file:
        print(line.strip())
#Section F — CSV Processing Without Pandas
import csv
with open("registrations.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    registrations = list(reader)
print(registrations)
print("Confirmed Registrations:")
for registration in registrations:
    if registration["status"] == "Confirmed":
        print(registration)
print("Hyderabad Registrations:")
for registration in registrations:
    if registration["city"] == "Hyderabad":
        print(registration)
for registration in registrations:
    registration["amount"] = float(registration["amount"])
print(registrations)
print("Registrations Above 7000:")
for registration in registrations:
    if registration["amount"] > 7000:
        print(registration)
total_amount = 0
for registration in registrations:
    total_amount += registration["amount"]
print("Total Registration Amount:", total_amount)
cities = []
for registration in registrations:
    cities.append(registration["city"])
unique_cities = set(cities)
print(unique_cities)

#Section G — JSON Processing
import json
with open("staff.json", "r") as file:
    staff = json.load(file)
print(type(staff))
for employee in staff:
    print(employee["name"])
for employee in staff:
    if employee["department"] == "Operations":
        print(employee["name"])
for employee in staff:
    if employee["salary"] > 75000:
        print(employee["name"], employee["salary"])
for employee in staff:
    if "Python" in employee["skills"]:
        print(employee["name"])
for employee in staff:
    print("Name:", employee["name"])
    print("Rating:", employee["performance"]["rating"])
    print(
        "Events Handled:",
        employee["performance"]["events_handled"]
    )
    print("--------------------")
for employee in staff:
    if employee["performance"]["rating"] > 4.5:
        print(employee["name"])
all_skills = []
for employee in staff:
    all_skills.extend(employee["skills"])
print(all_skills)
unique_skills = set(all_skills)
print(unique_skills)
salary_sorted = sorted(
    staff,
    key=lambda x: x["salary"],
    reverse=True
)
for employee in salary_sorted:
    print(employee["name"], employee["salary"])
rating_sorted = sorted(
    staff,
    key=lambda x: x["performance"]["rating"],
    reverse=True
)
for employee in rating_sorted:
    print(
        employee["name"],
        employee["performance"]["rating"]
    )
for employee in staff:
    if employee["staff_id"] == 503:
        employee["skills"].append("Pandas")
with open("staff_updated.json", "w") as file:
    json.dump(staff, file, indent=4)
print("Updated staff JSON created successfully")

#Section H — User-Defined Modules
#in event_utils.py and main.py

#Section I — Pandas Basics
import pandas as pd
registrations_df = pd.read_csv("registrations.csv")
print(registrations_df)
print("First 5 Rows:")
print(registrations_df.head())
print("Last 5 Rows:")
print(registrations_df.tail())
print("Shape:")
print(registrations_df.shape)
print("Columns:")
print(registrations_df.columns)
print("Datatypes:")
print(registrations_df.dtypes)
print(
    registrations_df[
        [
            "attendee_name",
            "city",
            "status",
            "amount"
        ]
    ]
)

confirmed_df = registrations_df.query(
    "status == 'Confirmed'"
)
print(confirmed_df)
high_amount_df = registrations_df[
    registrations_df["amount"] > 6000
]
print(high_amount_df)
hyderabad_confirmed = registrations_df[
    (registrations_df["status"] == "Confirmed") &
    (registrations_df["city"] == "Hyderabad")
]
print(hyderabad_confirmed)
status_count = registrations_df["status"].value_counts()
print(status_count)
status_amount = registrations_df.groupby(
    "status"
)["amount"].sum()
print(status_amount)
city_average = registrations_df.groupby(
    "city"
)["amount"].mean()
print(city_average)