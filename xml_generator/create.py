from .element_creator import *
from .prettify import *


def create(data):
    """Return prettify XML string for the given 'data'
    """
    root_attributes = {
        'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'xsi:schemaLocation': 'http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd'
    }
    root = create_parent('urlset', root_attributes)

    for url in data:
        url_elem = create_parent('url')
        loc_child = create_child(url_elem, 'loc', url)
        lastmod_child = create_child(url_elem, 'last_mod', '')
        priority_child = create_child(url_elem, 'priority', 1)
        root = set_child(root, url_elem)

    return prettify(root)
