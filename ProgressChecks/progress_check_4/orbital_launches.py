import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

if __name__ == '__main__':
    launch_site_countries = {
        'Ba': 'Kazakhstan',
        'BC': 'USA',
        'CC': 'USA',
        'CCK': 'USA',
        'HCS': 'China',
        'Jq': 'China',
        'Jej': 'South Korea',
        'Kd': 'USA',
        'Kii': 'Japan',
        'Ko': 'France',
        'Na': 'South Korea',
        'OnS': 'New Zealand',
        'Pl': 'Russia',
        'Sem': 'Iran',
        'Shr': 'Iran',
        'So': 'North Korea',
        'Sr': 'India',
        'Ta': 'Japan',
        'TY': 'China',
        'Va': 'USA',
        'Vo': 'Russia',
        'We': 'China',
        'WI': 'USA',
        'Xi': 'China'
    }
    response = requests.get("https://space.skyrocket.de/doc_chr/lau2024.htm")
    responseText = response.text
    soup = BeautifulSoup(responseText,"html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    dictCounts = {}
    for row in rows:
        cells = row.find_all("td")
        if len(cells) < 2:
            continue
        rowData = [cell.get_text() for cell in cells]
        launchSite = rowData[-2].strip()
        if launchSite.startswith("Xi"):
            launchSite = "Xi"
        if launchSite[0:3] in dictCounts:
            dictCounts[launchSite[0:3]] += 1
        else:
            dictCounts[launchSite[0:3]] = 1
    sortedDict = sorted(dictCounts.items())
    #launch_sites
    categories = [item[0].strip() for item in sortedDict]
    yPoints = [item[1] for item in sortedDict]
    plt.clf()
    plt.bar(categories,yPoints)
    plt.savefig("launch_sites.output.png")
    plt.clf()
    #countries_key
    countries = {}
    """
        Algorithm for this part
        1. keys need to be the values in launch_site_countries.values()
        2. We need to call sorted() on our dictionary for items()
        3. .keys() of launch_site_countries returns the keys and those keys have values in dictCounts
    """
    strippedKeyDict = {key.strip(): value for key, value in dictCounts.items()}
    for key,value in launch_site_countries.items():
        if key in strippedKeyDict.keys():
            if launch_site_countries[key] in countries:
                countries[value] += strippedKeyDict.get(key)
            else:
                countries[value] = strippedKeyDict.get(key)
        else:
            continue
    sortedCountDict = sorted(countries.items())
    cats = [item[0] for item in sortedCountDict]
    ys = [item[1] for item in sortedCountDict]
    plt.bar(cats,ys)
    plt.savefig("countries.output.png")
    for key,value in strippedKeyDict.items():
        if key not in launch_site_countries.keys():
            print(f"{key}: {value}")










