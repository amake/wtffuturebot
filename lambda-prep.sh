#!/bin/bash -O extglob

if [ ! -d .env ]; then
    virtualenv .env
    .env/bin/pip install -e .
fi

if [ ! -f adjectives.txt ]; then
    echo "Required file adjectives.txt not found. Run getadjectives.py."
    exit 1
fi

if [ ! -f people.txt ]; then
    echo "Required file people.txt not found. Run getpeople.py."
    exit 1
fi


if [ -f lambda-deploy.zip ]; then
    rm lambda-deploy.zip
fi

zip lambda-deploy *.py *.json adjectives.txt people.txt -x \*.pyc

cd .env/lib/python2.7/site-packages
zip -r ../../../../lambda-deploy ./!(pip*|wheel*|setuptools*|easy_install*|pattern*|Pattern*|nltk*) \
    -x \*.pyc
