import os


def save(xml, path="sitemap.xml"):
    """Saves the 'xml' content into the filename specified in the 'path'
    """
    with open(path, "w") as f:
        f.write(xml)
        print(f)
