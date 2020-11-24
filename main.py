import datetime
from xml_generator.create import create
from xml_generator.save import save
from crawler.scraper import scrape


print("Scraping started...\n")
start_time = datetime.datetime.now()
data = scrape()

print("Scraping completed...\n")
end_time = datetime.datetime.now()

diff = end_time - start_time
m, s = divmod(diff.total_seconds(), 60)
print(f"Total time spent: {m//60}:{m%60}:{s}")

total_links = len(data)
print(f"Total {total_links} links found\n")
print(f"First link: {data[0]}\n")
print(f"Last link: {data[total_links - 1]}\n\n")

print("Creating sitemap.xml\n")
xml = create(data)
save(xml)
print("Created sitemap.xml\n\n")
