#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response
"""
import urllib.request as req
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    with req.urlopen(url) as respt:
        data = respt.info()
        print(data.get("X-Request-Id"))
