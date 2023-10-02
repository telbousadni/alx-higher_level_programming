#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status. """
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    res = requests.get(url)
    data = res.text
    resType = type(data)
    print(f"Body response:\n\t- type: {resType}\n\t\
- content: {data}")
