import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2209405.json'

print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")
info = json.loads(data)
nums = list()
for x in range(len(info['comments'])):
    nums.append(info['comments'][x]['count'])

print('Count:',len(nums))
print('Sum:', sum(nums))