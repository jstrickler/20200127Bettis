#!/usr/bin/env python
import lxml.etree as ET

"""
<presidents>
    <president term="1">
    <first_name>George</first_name>
</presidents>
"""

xml_root = ET.Element('presidents')

with open('DATA/presidents.txt') as pres_in:
    for line in pres_in:
        term, last_name, first_name, dob, dod, bplace, bstate, took_office, left_office, party = line.rstrip().split(':')
        p = ET.SubElement(xml_root, 'president', term=term)
        s = ET.SubElement(p, "first_name")
        s.text = first_name
        ET.SubElement(p, "last_name").text = last_name
        ET.SubElement(p, "party").text = party


xml_text = ET.tostring(xml_root, pretty_print=True).decode()
print(xml_text)

xml_doc = ET.ElementTree(xml_root)
xml_doc.write('presidents.xml', pretty_print=True, xml_declaration=True)




