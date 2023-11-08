import json

file = open("people.json", "r")
data = json.load(file)
print("User Count:", len(data["userdetails"]))
print(data)
for user in data["userdetails"]:
    print("Name:", user["name"])
    print("ID:", user["id"])
    print("X Value:", user["x"])
