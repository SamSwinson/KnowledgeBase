import xml.etree.ElementTree as et
employees=[{'name':'aaa','age':21,'sal':5000},{'name':"xyz",'age':22,'sal':6000}]
root = et.Element("employees")
for employee in employees:
    child=et.Element("employee")
    root.append(child)
    nm = et.SubElement(child, "name")
    nm.text = employee.get('name')
    age = et.SubElement(child, "age")
    age.text = str(employee.get('age'))
    sal= et.SubElement(child, "sal")
    sal.text=str(employee.get('sal'))

tree = et.ElementTree(root)
with open('employees.xml', "wb") as fh:
    tree.write(fh)
