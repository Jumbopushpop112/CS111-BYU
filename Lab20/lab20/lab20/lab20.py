import requests
import bs4

def download(url, output_filename):
    """*** YOUR CODE HERE ***"""
    response = requests.get(url)
    responseText = response.text
    with open(output_filename,"w") as file:
        file.write(responseText)

def make_pretty(url, output_filename):
    """*** YOUR CODE HERE ***"""
    response = requests.get(url)
    responseText = response.text
    soup = bs4.BeautifulSoup(responseText,features="html.parser")
    with open(output_filename,"w") as file:
        file.write(soup.prettify())

def find_paragraphs(url, output_filename):
    """*** YOUR CODE HERE ***"""
    response = requests.get(url)
    responseText = response.text
    soup = bs4.BeautifulSoup(responseText, features="html.parser")
    paragraphs = soup.find_all('p')
    with open(output_filename, "w") as file:
        for p in paragraphs:
            file.write(str(p))
            file.write("\n")
def find_links(url, output_filename):
    """*** YOUR CODE HERE ***"""
    response = requests.get(url)
    responseText = response.text
    soup = bs4.BeautifulSoup(responseText, features="html.parser")
    anchors = soup.find_all("a")
    with open(output_filename, "w") as file:
        for a in anchors:
            href = a.get('href')
            file.write(str(href))
            file.write("\n")
