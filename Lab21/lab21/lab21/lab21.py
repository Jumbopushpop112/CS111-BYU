# *WRITE YOUR CODE IN THIS FILE*
from urllib.parse import urlparse, urljoin
import requests
def get_domain(url):
    parsed = urlparse(url)
    if parsed.scheme not in ("https","http"):
        return ""
    else:
        return parsed.scheme + "://" + parsed.netloc

def combine_paths(url, path):
    parsed = urlparse(url)
    return parsed.scheme + "://" + parsed.netloc + path

def combine_urls(url1,url2):
    return urljoin(url1,url2)

def print_pages(url, pathPageList, outputFile):
    with open(outputFile,"w") as file:
        new_path = url
        for item in pathPageList:
            new_path = urljoin(new_path,item)
            result = requests.get(new_path)
            file.write(result.text)
            file.write("\n")









