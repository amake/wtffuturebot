from __future__ import print_function
import os
import sys
import json

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

with open('google_credentials.json') as infile:
    credentials = json.load(infile)

search_url = 'https://www.googleapis.com/customsearch/v1'
auth_params = {'key': credentials['GoogleKey'],
               'cx': credentials['GoogleID']}

def search_images(q):
    params = {'searchType': 'image',
              'imgSize': 'xxlarge',
              'imgType': 'photo',
              'imgColorType': 'color',
              'q': q}
    params.update(auth_params)
    url = search_url + '?' + urlencode(params)
    response = urlopen(url).read()
    return [item['link'] for item in json.loads(response)['items']]
