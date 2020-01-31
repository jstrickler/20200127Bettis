#!/usr/bin/env python
import lxml.etree as ET

doc = ET.parse('presidents.xml')

print(doc)

root = doc.getroot()
print(root)

for president in root.findall('president'):
    first_name = president.findtext('first_name')
    last_name = president.findtext('last_name')
    party = president.findtext('party')
    print(first_name, last_name, party)
print('-' * 60)


for party in root.findall('.//party'):
    print(party.text)
print('-' * 60)

for thing in root.iter():
    print(thing.tag)
