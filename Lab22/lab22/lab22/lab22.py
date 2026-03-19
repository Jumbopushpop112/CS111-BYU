import requests
import bs4
import urllib.parse
import sys
def scavengerHunt(url,element,attribute, outputFile):
    response = requests.get(url)
    responseText = response.text
    soup = bs4.BeautifulSoup(responseText, features="html.parser")
    listTags = soup.find_all(element)
    for tag in listTags:
        if tag.has_attr(attribute):
            foundTag = tag.attrs
            foundAttribute = foundTag[attribute]
            if attribute == "final":
                with open(outputFile,"w") as file:
                    file.write(foundAttribute)
                return
            listAttribute = foundAttribute.split(",")
            curUrl = listAttribute[0]
            curTag = listAttribute[1]
            curAttribute = listAttribute[2]
            scavengerHunt(curUrl, curTag, curAttribute, outputFile)
def main():
    scavengerHunt(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
main()