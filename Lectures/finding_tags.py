import bs4
import re

if __name__ == "__main__":
    s = """<html>
  <head>
      <title data="extra stuff">Hello world!</title>
  </head>
  <body>
    <h1 id="header">Hello world!</h1>
    <p id="data999">This is a simple <em>hello world</em> web page.</p>
    <p id="start">This paragraph has an absolute link to the <a href="https://cs111.byu.edu">CS 111 Homepage</a> in it.</p>
    <p>This paragraph has a domain relative link to <a href="/proj/proj4">Project 4</a>.</p>
    <p id="start" data="index">This paragraph has a page relative link to <a href="HW/HW07">Homework 7</a>.</p>
    <p>This paragraph has an image after it.</p>
    <img height="200" src="cougar.png">
    <p>Below is a table with the squares and cubes of the first six integers</p>
    <table>
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

    soup = bs4.BeautifulSoup(s, "html.parser")

    print(soup.find_all('img',height=True))
    
    print(soup.find_all('tr', {'id': 'data'}))
    print(soup.find_all('tr', id='data'))

    print(soup.find_all(['p', 'h1'], {'id':True}))

    print(soup.find_all(['h1', 'tr'], {'id': 'header'}))
    
    print(soup.find_all(['h1', 'tr', 'p'],
                         {'id': 'header'}, {'data': 'index'}))

    print(soup.find_all(['h1', 'tr', 'p'],
                         {'id': ['header', 'start'], 'data': 'index'}))

    print(soup.find_all(['td', 'p'],
                         {'id': re.compile(r'data\d*')}))

    data_index = re.compile(r'data\d*')
    print(soup.find_all(['td', 'p', 'tr'],
                         {'id': data_index, 'title': data_index}))
