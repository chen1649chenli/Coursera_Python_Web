import urllib
from BeautifulSoup import *

url = raw_input('Enter url:')
count = int(raw_input('Enter count:'))
position = int(raw_input("Enter position:")) -1
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

i = 0
while i < count:
    url = tags[position].get('href', None)
    print tags[position].text
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    i = i + 1
