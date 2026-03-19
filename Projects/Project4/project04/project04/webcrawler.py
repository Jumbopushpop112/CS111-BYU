import requests
import bs4
from urllib.parse import urljoin
import urllib
import matplotlib.pyplot as plt
from image_processing import sepia, grayscale, flipped, mirror
from RequestGuard import RequestGuard
import sys
"""
Count our links and plot them with the provided data
"""
def countLinks(url,outputFile1,outputFile2):
    requestGuard = RequestGuard(url)
    #Add the link to the list of links to visit
    linksToVisit = []
    dictLinks = {url:1}
    linksToVisit.append(url)
    while len(linksToVisit) != 0:
        link = linksToVisit.pop(0)
        page = requestGuard.make_get_request(link)
        html = bs4.BeautifulSoup(page.text, "html.parser")
        for tag in html.find_all('a'):
            href = tag.get('href')
            newURL = urljoin(link,href)
            if "#" in href:
                newURL = newURL.split("#")[0]
            if newURL in dictLinks:
                dictLinks[newURL] +=1
            else:
                dictLinks[newURL] = 1
                if requestGuard.can_follow_link(newURL):
                    linksToVisit.append(newURL)
    listData = list(dictLinks.values())
    listBins = [item for item in range(min(listData),max(listData)+2)]
    n, bins, patches = plt.hist(listData,listBins)
    plt.savefig(outputFile1)
    plt.clf()
    with open(outputFile2, "w") as file:
        for i in range(len(n)):
            file.write(f"{float(bins[i])},{float(n[i])}\n")
            i+=1
    return dictLinks
"""
Give a URL, extract the table from the site and plot the appropriate data
"""
def extractAndPlotTable(url,outputFile1,outputFile2):
    requestGuard = RequestGuard(url)
    response = requestGuard.make_get_request(url)
    if not response:
        print("Page does not exist!")
        return
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    tableId = "CS111-Project4b"
    table = soup.find("table",{"id":tableId})
    rows = table.find_all("tr")
    xValues = []
    yValues1 = []
    yValues2 = []
    yValues3 = []
    yValues4 = []
    for row in rows:
        columns = row.find_all("td")
        if len(columns) == 2:
            xValues.append(float(columns[0].get_text()))
            yValues1.append(float(columns[1].get_text()))
        elif len(columns) == 3:
            xValues.append(float(columns[0].get_text()))
            yValues1.append(float(columns[1].get_text()))
            yValues2.append(float(columns[2].get_text()))
        elif len(columns) == 4:
            xValues.append(float(columns[0].get_text()))
            yValues1.append(float(columns[1].get_text()))
            yValues2.append(float(columns[2].get_text()))
            yValues3.append(float(columns[3].get_text()))
        elif len(columns) == 5:
            xValues.append(float(columns[0].get_text()))
            yValues1.append(float(columns[1].get_text()))
            yValues2.append(float(columns[2].get_text()))
            yValues3.append(float(columns[3].get_text()))
            yValues4.append(float(columns[4].get_text()))
    if yValues1:
        plt.plot(xValues,yValues1,"b")
    if yValues2:
        plt.plot(xValues,yValues2,"g")
    if yValues3:
        plt.plot(xValues,yValues3,"r")
    if yValues4:
        plt.plot(xValues,yValues4,"k")

    plt.savefig(outputFile1)
    with open(outputFile2,"w") as file:
        for i in range(len(xValues)):
            file.write(f"{xValues[i]}")
            if yValues1:
                file.write(f",{yValues1[i]}")
            if yValues2:
                file.write(f",{yValues2[i]}")
            if yValues3:
                file.write(f",{yValues3[i]}")
            if yValues4:
                file.write(f",{yValues4[i]}")
            file.write("\n")
"""
Modify the appropriate images give a filter, and a url containing images
"""
def modifyImages(url, convention, filter):
    requestGuard = RequestGuard(url)
    response = requestGuard.make_get_request(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    listImages = soup.find_all("img")
    imageSources = []
    for image in listImages:
        source = image.get("src")
        if source:
            urlSource = urljoin(url,source)
            imageSources.append(urlSource)
    for imageSource in imageSources:
        listImageSource = imageSource.split("/")
        neededSource = listImageSource[len(listImageSource)-1]
        response = requestGuard.make_get_request(imageSource)
        outputFileName = convention + neededSource
        with open(outputFileName, 'wb') as outputFile:
            outputFile.write(response.content)
        if filter == "-s":
            sepia(outputFileName,outputFileName)
        elif filter == "-g":
            grayscale(outputFileName,outputFileName)
        elif filter == "-f":
            flipped(outputFileName,outputFileName)
        else:
            mirror(outputFileName,outputFileName)
"""
main function that does all the magic 
"""
def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ["-c", "-p", "-i"]:
        print("invalid arguments")
        return
    #count links function
    if sys.argv[1] == "-c":
        if len(sys.argv) != 5:
            print("Invalid arguments")
            return
        countLinks(sys.argv[2],sys.argv[3],sys.argv[4])
    #extract and plot tables function
    elif sys.argv[1] == "-p":
        if len(sys.argv) != 5:
            print("Invalid arguments")
            return
        extractAndPlotTable(sys.argv[2],sys.argv[3],sys.argv[4])
    #image download and processing
    elif sys.argv[1] == "-i":
        if len(sys.argv) != 5 or sys.argv[4] not in ["-s", "-g", "-f", "-m"]:
            print("Invalid arguments")
            return
        modifyImages(sys.argv[2],sys.argv[3],sys.argv[4])
"""
call the main function 
"""
if __name__ == "__main__":
    main()