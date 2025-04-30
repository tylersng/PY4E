import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def webget(url):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    x =[tag.get('href', None) for tag in tags]
    return x 

url = input('Enter - ')
x = webget(url)
count = input('Enter count: ')
pos = input('Enter position: ')
i = 0 
ic = int(count)
ipos = int(pos) - 1
while i < int(count): 
    if i == 0:
        print("Retrieving: ",url)
        print("Retrieving: ",x[ipos])
        i = i + 1 
    else:
        x = webget(x[ipos])
        print("Retrieving: ",x[ipos])
        i = i + 1