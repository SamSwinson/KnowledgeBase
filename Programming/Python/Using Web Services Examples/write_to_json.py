import json

numusers = int(input("Number of employees to: "))
count = 0
employees = dict()
employee = dict()

while count < numusers:
    name = input("Enter the employee name: ")
    email = input("Enter the employee email: ")
    id = input("Enter the employee id: ")
    employee["name"] = name
    employee["email"] = email
    employee["id"] = id
    employees[count] = employee
    count += 1

json_object = json.dumps(employees, indent = 3)

with open("employees.json", "w") as outfile:
    outfile.write(json_object)
