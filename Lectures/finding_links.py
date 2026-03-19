import requests
from bs4 import BeautifulSoup

URL = "https://cs111.byu.edu"
resp = requests.get(URL)
soup = BeautifulSoup(resp.text,"html.parser")
aTags = soup.find_all("a")
count_absolute = 0
count_domain_relative = 0
count_page_relative = 0
count_section = 0
count_mailto = 0
for tag in aTags:
    link = tag.get("href") #or tag.attrs["href"]
    if not link:
        continue
    #do something with the link here
    print(f"{tag.string} => {link}")
    #compute the counts of the various type of links here
    if "mailto" in link:
        count_mailto += 1
    elif "#" in link:
        count_section +=1
    elif "http" in link:
        count_absolute +=1
    elif link.startswith("/"):
        count_domain_relative += 1
    else:
        count_page_relative += 1
print(f'count_absolute = {count_absolute}')
print(f'count_domain_relative = {count_domain_relative}')
print(f'count_page_relative = {count_page_relative}')
print(f'count_section = {count_section}')
print(f'count_mailto = {count_mailto}')
