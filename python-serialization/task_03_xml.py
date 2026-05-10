#!/usr/bin/python3
"""XML serialization/desrlztion module"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Py dict -> XML"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """XML -> Py dict"""
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        if child.text is not None:
            result[child.tag] = child.text
        else:
            result[child.tag] = ""
    
    return result
