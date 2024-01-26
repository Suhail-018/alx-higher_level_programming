#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
import urllib.request as req
import urllib.parse as parse
import sys



if __name__ == "__main__":
   
    url = sys.argv[1]
    email = sys.argv[2]

    value = {"email": email}

    data_req = parse.urlencode(value)
    data_req = data_req.encode('utf-8')

    re = req.Request(url, data_req)

    with req.urlopen(re) as respt:
        data = respt.read()
        print(data.decode())
