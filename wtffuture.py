from __future__ import print_function
import os
import sys
import random
import search

adjectives = []
people = []

def load_words(filename):
    if os.path.isfile(filename):
        with open(filename) as f:
            return f.read().splitlines()
    else:
        print(filename + ' not found. Generate it.')
        sys.exit(1)

adjectives = load_words('adjectives.txt')
people = load_words('people.txt')

allowed_image_formats = ['gif', 'jpeg', 'jpg', 'png']

def _random_future_text():
    return 'This is the future that %s want' % random.choice(people)

def _random_image_urls():
    for _ in xrange(10):
        q = '%s future' % random.choice(adjectives)
        images = [img for img in search.search_images(q)
                  if any(img.endswith(ext) for ext in allowed_image_formats)]
        if images:
            random.shuffle(images)
            return images, q
    raise Exception('Failed to find images')

def random_future():
    return (_random_future_text(),) + _random_image_urls()

if __name__ == '__main__':
    for _ in xrange(10):
        print(_random_future_text())
