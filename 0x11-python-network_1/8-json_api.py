#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == '__main__':

    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}

    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json = r.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))

    except ValueError:
        print("Not a valid JSON")
