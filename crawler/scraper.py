from urllib.request import urlopen
from bs4 import BeautifulSoup


seed_url = "https://www.whenabongcooks.com"


def scrape(url=seed_url):
    results = []

    soup = get_html_content(url)
    links = get_anchor_elements(soup)
    # links = sanitize_data(links)

    while len(links) != 0:
        each_link = links[0]
        if each_link not in results and "whenabongcooks.com/" in each_link:
            results.append(each_link)
            s = get_html_content(each_link)
            if s != "":
                new_list_of_links = get_anchor_elements(s)

                links.extend(new_list_of_links)
                links = remove_items(links, each_link)

                links = remove_duplicate(links)

                print(f"Results: {len(results)}, Links: {len(links)}\n")

        links = remove_items(links, each_link)

    results = sanitize_data(results)
    return results


def get_html_content(url):
    html = ""
    try:
        response = urlopen(url)
        if response.getcode() == 200:
            html = BeautifulSoup(response, 'html5lib')
    except:
        pass

    return html


def get_anchor_elements(soup):
    return [i['href'] for i in soup.findAll('a', href=True)]


def remove_items(list_of_links, item):
    return [i for i in list_of_links if i != item]


def remove_duplicate(list_of_links):
    return list(dict.fromkeys(list_of_links))


def sanitize_data(list_of_links):
    return [char for char in list_of_links if "#" not in char]
