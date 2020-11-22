from urllib.request import urlopen
from bs4 import BeautifulSoup

seed_url = "https://www.whenabongcooks.com"


def scrape(url=seed_url):
    results = []

    soup = get_html_content(url)
    links = get_anchor_elements(soup)

    while len(links) != 0:
        each_link = links[0]
        if each_link not in results and "whenabongcooks.com/" in each_link:
            results.append(each_link)
            s = get_html_content(each_link)
            if s != "":
                new_list_of_links = get_anchor_elements(s)

                old_len = len(links)

                links.extend(new_list_of_links)
                links = remove_items(links, each_link)

                new_len = len(links)
                print(f"Links length: {len(links)} ({new_len - old_len}) \n")
        else:
            links = remove_items(links, each_link)

    return results


def get_html_content(url):
    html = ""
    response = urlopen(url)
    if response.getcode() == 200:
        html = BeautifulSoup(response, 'html5lib')

    return html


def get_anchor_elements(soup):
    return [i['href'] for i in soup.findAll('a', href=True)]


def remove_items(list_of_links, item):
    return [i for i in list_of_links if i != item]
