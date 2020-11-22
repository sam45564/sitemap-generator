import datetime
from xml_generator.create import create
from crawler.scraper import scrape

# data = ['some value', 'another value', 'some more value']
# results = create(data)
print("Scraping started...\n")
start_time = datetime.datetime.now()
results = scrape()

print("Scraping completed...\n")
end_time = datetime.datetime.now()

diff = end_time - start_time
m, s = divmod(diff.total_seconds(), 60)
print(f"Total time spent: {m//60}:{m%60}:{s}")

total_links = len(results)
print(f"Total {total_links} links found\n")
print(f"First link: {results[0]}\n")
print(f"Last link: {results[total_links - 1]}\n\n")
