from bs4 import BeautifulSoup
from urllib import request, parse

results = []


def scrape(seed_url):
    """Scrapes the given url(seed_url) for retreiving the links."""
    links = []

    # Get initial list of anchors from the seed_url
    html = get_html(seed_url)
    if html != "":
        links = get_anchors(html)

    # Iterate over the list of initial anchors and check if they are in results. If not add into list.
    while len(links) > 0:
        links = sanitize_before_processing(links, results, seed_url)

        pass


def get_html(url):
    """Returns html content for the given url"""
    html = ""
    try:
        response = request.urlopen(url)
        if response.code != 200:
            html = BeautifulSoup(response, 'html5lib')
    except:
        print(f"Could not fetch data for the url: {url}")

    return html


def get_anchors(html):
    """Returns list of anchors for the given html soup"""
    return [a['href'] for a in html.findAll('a', href=True)]


def sanitize_before_processing(data, result, seed_url):
    """Returns data without duplicate values and unwanted urls"""
    host = parse.urlparse(seed_url)
    # Removes duplicates in the list
    data = list(dict.fromkeys(data))

    # Excluding url if it doesn't contain seed_url or contains '#' or is already present in final 'result'
    data = [
        url for url in data if host.netloc in url and url not in result and "#" not in url]

    return data
