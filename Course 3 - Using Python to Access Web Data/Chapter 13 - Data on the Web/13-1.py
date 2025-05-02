import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2209404.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url).read()
print('Retrieved',len(uh),'characters')
tree = ET.fromstring(uh)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))
