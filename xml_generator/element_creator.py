from xml.etree.ElementTree import Element, SubElement


def create_parent(parent_name, attribute_dict=''):
    """Returns parent element for an XML tree.
    """
    parent = Element(parent_name)
    if attribute_dict != '':
        for key in attribute_dict:
            parent.set(key, attribute_dict[key])
    return parent


def create_child(parent_name, child_name, text_in_child=''):
    """Returns child element for a given parent and assigns text if available.
    """
    child = SubElement(parent_name, child_name)
    if text_in_child != '':
        child.text = text_in_child
    return child


def set_child(parent_element, child_element):
    """Sets child element for a given parent element.
    """
    parent_element = SubElement(parent_element, child_element)
    return parent_element
