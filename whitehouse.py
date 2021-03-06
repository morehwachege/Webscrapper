import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefing-room/statements-releases/")
src = result.content
soup = BeautifulSoup(src, 'lxml')
urls = []
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')
    if a_tag is not None:
        urls.append(a_tag.attrs['href'])

for url in urls:
    print(url)
