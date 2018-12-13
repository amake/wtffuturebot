from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wtffuturebot',
    version='1.0',
    description='A bot to tweet portents of the future',
    long_description=long_description,
    url='https://github.com/amake/wtffuturebot',
    author='Aaron Madlon-Kay',
    author_email='aaron@madlon-kay.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='future portents',
    py_modules=['wtffuture', 'search', 'bot', 'getadjectives', 'getpeople'],
    install_requires=['tweepy', 'nltk', 'pattern']
)
