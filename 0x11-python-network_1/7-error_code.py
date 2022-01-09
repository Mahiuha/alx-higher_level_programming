#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and manage errors
"""
import requests
import sys

if __name__ == '__main__':

    res = requests.get(sys.argv[1])

    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
