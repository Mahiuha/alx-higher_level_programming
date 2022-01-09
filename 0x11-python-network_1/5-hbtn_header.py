#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id
"""
import requests
import sys

if __name__ == '__main__':

    res = requests.get(sys.argv[1])
    head = res.headers.get('X-Request-Id')
    print(head)
