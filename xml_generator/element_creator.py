from xml.etree.ElementTree import Element, SubElement
from xml.dom import minidom


def create_element(element_name, element_text='', attributes=''):
    new_element = Element(element_name)

    if element_text != '':
        new_element.text = element_text

    if attributes != '':
        for key in attributes:
            new_element.set(key, attributes[key])

    return new_element


def append_element(parent, child):
    return parent.append(child)
