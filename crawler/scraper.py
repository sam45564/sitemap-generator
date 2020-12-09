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

        if len(links) > 0:
            current_link = links.pop(0)
            if current_link not in results:
                results.append(current_link)

            html = get_html(current_link)
            if html != "":
                new_links = get_anchors(html)
                links = links + new_links

        print(f"Total links to be processed: {len(links)}")
        print(f"Total links in final result: {len(results)}\n")

    return results


def get_html(url):
    """Returns html content for the given url"""
    html = ""
    try:
        response = request.urlopen(url)
        if response.code == 200:
            html = BeautifulSoup(response, 'html5lib')
        if response.code != 200:
            print(f"Got {response.code} for {url}\n")
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
    # NOTE: The conditions in the following list comprehension is specific for a specific website.
    # Modify the conditions if they are not suitable for your requirements.
    data = [
        url for url in data if host.netloc in url and url not in result and "#" not in url and "https://www.addtoany.com/" not in url]

    return data
