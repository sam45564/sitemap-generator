from crawler.scraper import scrape
from xml_generator.create import create
from xml_generator.save import save

seed_url = "https://www.whenabongcooks.com"


print("Scraping started...\n")
data = scrape(seed_url)

print("Scraping completed...\n")

total_links = len(data)
print(f"Total {total_links} links found\n")
print(f"First link: {data[0]}\n")
print(f"Last link: {data[total_links - 1]}\n\n")

print("Creating sitemap.xml\n")
xml = create(data)
save(xml)
print("Created sitemap.xml\n\n")
