#!/usr/bin/python3
"""  fetches https://intranet.hbtn.io/status  """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        r = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(r.decode("UTF-8")))
