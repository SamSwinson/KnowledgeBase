import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='people.xml')
users = tree.findall("persons/user")
print ("User Count:", len(users))
for user in users:
    print("User:", user.get("x"))
    print("Name:", user.find('name').text)
    print("ID:", user.find('id').text)
    print("Email:", user.find('email').text)
    print("Domain:", user.find('domain').text)
