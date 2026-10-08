cities = {"Hyderabad", "Mumbai", "Delhi", "Hyderabad"}

print(cities)

cities1 = [
"Hyderabad",
"Mumbai",
"Delhi",
"Hyderabad",
"Mumbai"
]


unique_cities = set(cities1)

print(unique_cities)
cities.add("Pune")

cities.remove("Mumbai")

#Safer Option to Remove
cities.discard("Chennai")