import xml.etree.ElementTree as ET

tree = ET.parse('techCrunchRSS.xml')
root = tree.getroot()

print(root.tag)
print(len(root))

print(len(root[0]))