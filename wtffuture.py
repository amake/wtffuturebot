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

def _random_future():
    return 'This is the future that %s want' % random.choice(people)

def _random_image():
    q = '%s future' % random.choice(adjectives)
    images = search.search_images(q)
    return q, random.choice(images)

def random_future():
    _, img = _random_image()
    return _random_future(), img

if __name__ == '__main__':
    for _ in xrange(10):
        print(_random_future())
