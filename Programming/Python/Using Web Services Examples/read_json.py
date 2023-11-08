import json

file = open("json.json", "r")
data = json.load(file)
print("Name:", data["name"])
print("Hide:", data["email"]["hide"])
