import bs4
import requests
from io import BytesIO
from PIL import Image

s = """<html>
  <head>
      <title data="extra stuff">Hello world!</title>
  </head>
  <body>
    <h1 id="header">Hello world!</h1>
    <p id="data999">This is a simple <em>hello world</em> web page.</p>
    <p id="start">This paragraph has a link to the <a href="https://cs111.byu.edu">CS 111 Homepage</a> in it.</p>
    <p>This paragraph has a domain relative link to <a href="/proj/proj4">Project 4</a>.</p>
    <p id="start" data="index">This paragraph has a page relative link to <a href="HW/HW07">Homework 7</a>.</p>
    <p>This paragraph has an image after it.</p>
    <img height="200" src="cougar.png">
    <p>Below is a table with the squares and cubes of the first six integers</p>
    <table id="math">
      <tr id="header"><th>X</th><th>Y1</th><th>Y2</th></tr>
      <tr title="data" id="data0"><td id="data00">1</td><td id="data01">1</td><td id="data02">1</td></tr>
      <tr id="data"><td>2</td><td>4</td><td>8</td></tr>
      <tr><td>3</td><td>9</td><td>27</td></tr>
      <tr><td>4</td><td>16</td><td>64</td></tr>
      <tr><td>5</td><td>25</td><td>125</td></tr>
      <tr><td>6</td><td>36</td><td>216</td></tr>
    </table>
    <table id="degrees" border="1">
      <tr><th>Academic Year</th><th>Bachelors</th><th>Masters</th><th>Doctoral</th><th>Total</th></tr>
      <tr><td>2021-2022</td><td>6406</td><td>1128</td><td>233</td><td>7767</td></tr>
      <tr><td>2020-2021</td><td>6683</td><td>959</td><td>192</td><td>7834</td></tr>
      <tr><td>2019-2022</td><td>6684</td><td>1033</td><td>212</td><td>7929</td></tr>
      <tr><td>1896-1897</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>
    </table>
  </body>
</html>
"""

# get the right table
soup = bs4.BeautifulSoup(s, "html.parser")
table = soup.find_all('table', {"id":"degrees"})[0]
print(table)

# EXTRACT THE DATA FROM THE TABLE

# get the header labels in the table and put them in a list
headers = []
htags = table.find_all("th")
for tag in htags:
    headers.append(tag.string) # append the string attribute of each header tag to the list of headers
print(headers) # print the header strings

# now let's get the data items from each row and put them into lists for each column
data = [[], [], [], [], []]   # create a list of empty lists, one for each of the five columns
rows = table.find_all('tr') # get all the rows
for row in rows:
    columns = row.find_all("td")  # get the data items in each column in the row
    index = 0   # initialize the index into data to reference the sublist for each column
    for col in columns:
        data[index].append(col.string) # append the string attribute of the data item in each column to the list for that column in data
        index += 1
for col in data:
    print(col) # print the list containing the data items in each column

# EXTRACT THE LINKS TO ALL THE IMAGES ON A WEB SITE

request = requests.get("https://cs111.byu.edu/staff/")
soup = bs4.BeautifulSoup(request.text,"html.parser")
images = soup.find_all('img')
img_srcs = []
for img in images:
    img_srcs.append(img['src']) # append each image link to img_srcs from the src attribute on the img
for src in img_srcs:
    print(src) # print the links

# GET AN IMAGE, SAVE IT LOCALLY, AND SHOW IT

imageURL = "https://cs111.byu.edu/assets/images/staff/Steve_Richardson.jpg"
image_response = requests.get(imageURL, stream=True)
parts = imageURL.split("/")
output_filename = "output/" + parts[-1]
print(output_filename)
with open(output_filename, 'wb') as out_file:
    out_file.write(image_response.content)

image = Image.open(BytesIO(image_response.content))
image.show()

del image_response    # this frees up the memory (optional)
