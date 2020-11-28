from urllib.request import urlopen
from bs4 import BeautifulSoup
# import threading
# import logging

result = []
process_queue = []
threads = []


def scrape(url):
    """Crawls the given url"""
    process_queue = get_anchors(get_html(url))

    while len(process_queue) != 0:
        try:
            print(f"--> Total items to be processed: {len(process_queue)}")
            current_anchor = manage_queue(process_queue)
            if is_acceptable(result, current_anchor):
                result.append(current_anchor)
                print(f"--> Added: {current_anchor}")

                new_anchors = get_anchors(get_html(current_anchor))
                process_queue = purge_duplicates(
                    manage_queue(process_queue, new_anchors))
                print(f"--> Added {len(new_anchors)} into the queue")
            else:
                print(f"Skipped {current_anchor}\n")
        except:
            pass

    return purge_duplicates(result)


def get_html(url):
    """Return html content of the given url."""
    html = ""
    try:
        response = urlopen(url)
        if response.getcode() == 200:
            html = BeautifulSoup(response, 'html5lib')
    except:
        pass

    return html


def get_anchors(html):
    """Returns all the anchors from the given html."""
    return [anchor['href'] for anchor in html.findAll('a', href=True)]


def purge_duplicates(result):
    """Removes duplicate items from the final list of anchors"""
    return list(dict.fromkeys(result))


def manage_queue(process_queue, new_anchors=None):
    """Adds or removes the item from process queue list."""
    if new_anchors != None:
        process_queue.extend(new_anchors)
        return process_queue
    else:
        return process_queue.pop(0)


def is_acceptable(final_list, url):
    """Returns True or False for a url that is to be processed."""
    return "whenabongcooks.com" in url and "#" not in url and url not in final_list
