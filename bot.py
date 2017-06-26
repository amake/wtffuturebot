from __future__ import print_function
import os
import sys
import json
import urllib2
import logging
from StringIO import StringIO
import tweepy
import wtffuture

creds_file = 'credentials.json'

credentials = {}

if os.path.isfile(creds_file):
    with open(creds_file) as infile:
        credentials = json.load(infile)
else:
    print('Credentials not found. Run auth_setup.py first.')
    sys.exit(1)

auth = tweepy.OAuthHandler(credentials['ConsumerKey'],
                           credentials['ConsumerSecret'])
auth.set_access_token(credentials['AccessToken'],
                      credentials['AccessSecret'])

api = tweepy.API(auth)

def do_tweet(event, context):
    text, img_urls, img_flavor = wtffuture.random_future()
    for img_url in img_urls:
        try:
            f = StringIO(urllib2.urlopen(img_url).read())
            api.update_with_media(img_url, status=text, file=f)
            return text, img_url, img_flavor
        except Exception, e:
            logging.exception(e)
    raise Exception('Failed to tweet')

if __name__ == '__main__':
    print(do_tweet(None, None))
