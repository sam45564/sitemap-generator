from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elements):
    """Returns a pretty-printed XML string for the 'element' passed.
    """
    elements_as_string = ElementTree.tostring(elements, 'utf-8')
    parsed_string = minidom.parseString(elements_as_string)
    return parsed_string.toprettyxml(indent=" ")
