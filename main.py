from crawler.scraper import scrape
from xml_generator.create import create
from xml_generator.save import save
from datetime import timedelta

# Add the website for which sitemap will be generated.
seed_url = "https://whenabongcooks.com/"


print("Scraping started...\n")
start = timedelta()
data = scrape(seed_url)

print("Scraping completed...\n")

total_links = len(data)
print(f"Total {total_links} links found\n")
print(f"First link: {data[0]}\n")
print(f"Last link: {data[total_links - 1]}\n\n")

print("Creating sitemap.xml\n")
xml = create(data)
save(xml)
end = timedelta()
print("Created sitemap.xml\n\n")
print(f"Time elapsed: {end - start}")
