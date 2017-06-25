import os
import sys
import json
import urllib2
from urllib import urlencode

creds_file = 'google_credentials.json'
credentials = {}

if os.path.isfile(creds_file):
    with open(creds_file) as infile:
        credentials = json.load(infile)
else:
    print('Google credentials not found.')
    sys.exit(1)

search_url = 'https://www.googleapis.com/customsearch/v1'
auth_params = {'key': credentials['GoogleKey'],
               'cx': credentials['GoogleID']}

def search_images(q):
    url = search_url + '?' + urlencode(dict(auth_params.items() +
                                            {'searchType': 'image',
                                             'q': q}.items()))
    response = urllib2.urlopen(url).read()
    return [item['link'] for item in json.loads(response)['items']]
