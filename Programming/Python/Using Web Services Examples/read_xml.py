import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='xml.xml')
print("Name:", tree.find('name').text)
print("ID:", tree.find('id').text)
