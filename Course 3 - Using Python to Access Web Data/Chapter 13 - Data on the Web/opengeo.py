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
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters',data[:20].replace('\n', ' '))
    try: 
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('=== Download Error ===')
        print(data)
        break
    if len(js['features']) == 0:
        print('=== Object not found ===')
        break
    
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)         