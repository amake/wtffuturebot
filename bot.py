from __future__ import print_function
import os
import sys
import json
import logging
import tweepy
import wtffuture
from io import BytesIO


try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

with open('credentials.json') as infile:
    credentials = json.load(infile)

auth = tweepy.OAuthHandler(credentials['ConsumerKey'],
                           credentials['ConsumerSecret'])
auth.set_access_token(credentials['AccessToken'],
                      credentials['AccessSecret'])

api = tweepy.API(auth)


def do_tweet(event, context):
    text, img_urls, img_flavor = wtffuture.random_future()
    for img_url in img_urls:
        try:
            f = BytesIO(urlopen(img_url).read())
            api.update_with_media(img_url, status=text, file=f)
            return text, img_url, img_flavor
        except Exception as e:
            logging.exception(e)
    raise Exception('Failed to tweet')


if __name__ == '__main__':
    print(do_tweet(None, None))
