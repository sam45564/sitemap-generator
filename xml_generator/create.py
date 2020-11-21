from .element_creator import *
from datetime import date, datetime
from .prettify import *


def create(url_list):
    """Return prettify XML string for the given 'url_list'
    """
    document_attributes = {
        'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'xsi:schemaLocation': 'http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd'
    }

    urlset = create_element('urlset', '', document_attributes)

    for url in url_list:
        url_elem = create_element('url')
        loc = append_element(url_elem, create_element('loc', url))
        last_modified = append_element(
            url_elem, create_element('lastmod', date.today().strftime(
                "%Y-%m-%dT") + datetime.now().strftime("%H:%M:%S+00:00")))
        priority = append_element(url_elem, create_element('priority', '1.00'))

        append_element(urlset, url_elem)

    return prettify(urlset)
