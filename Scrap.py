from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
countStr = input('Enter count: ')
positionStr = input('Enter position: ')

count = int(countStr)
position = int(positionStr)
i = 0

while i < count:
    print('Retrieving:', url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    o = 1

    for tag in tags:
        if o < position:
            o = o + 1
            continue

        url = tag.get('href', None)
        i = i + 1
        break

print('Retrieving:', url)
