#!/usr/bin/python3
""" takes in a URL and an email, sends a POST, displays the body of the
response (decoded in utf-8)"""

from urllib.request import Request, urlopen
import urllib.parse
from sys import argv

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')
    with urlopen(Request(argv[1], data)) as resp:
        print(resp.read().decode('utf-8'))
