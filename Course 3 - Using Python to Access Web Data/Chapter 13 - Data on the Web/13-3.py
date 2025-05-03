import urllib.request, urllib.parse
import json, ssl

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'
#ignore ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    address = input('Enter Location: ')
    if len(address) < 1: break
    address = address.strip()
    parms = dict()
    parms['q'] = address
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving',url)
    uh = urllib.request.urlopen(url, context= ctx)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')
    js = json.loads(data)
    print(js['features'][0]['properties']['plus_code'])