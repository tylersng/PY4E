from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    count.append(int(tag.contents[0]))
print("Count",len(count))
print("Sum",sum(count))