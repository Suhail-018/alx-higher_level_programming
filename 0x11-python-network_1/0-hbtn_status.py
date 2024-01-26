#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request as req


if __name__ == "__main__":
    from urllib import request as req

    with req.urlopen('https://alx-intranet.hbtn.io/status') as respt:
        data = respt.read()
        print("Body response:")
        print(f"\t- type: {type(data)}")
        print(f"\t- content: {data}")
        print(f"\t- utf8 content: {data.decode()}")
