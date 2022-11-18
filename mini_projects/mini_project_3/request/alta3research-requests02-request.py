#!/usr/bin/env python3

""" Mini_Project_2 Requests - WuTang Style
    This scrip makes a POST request for a new rapper"""

import requests
import json
from pprint import pprint

URL= "http://127.0.0.1:2224/"


new_rapper= {
    "name": "Clifford Smith Jr.",  
    "stageName": "Method Man",
    "aka": "Johnny Blaze",
    "association": "Wu-Tang Clan",
    "knownFor": "Mad different method to his style",
    "occupation": "Rapper/Songwriter/Record Producer/Actor",
    "hits": [
        "I'll Be There for You/You're All I Need to Get By",
        "Method Man",
        "C.R.E.A.M",
        "Protect Ya Neck",
        "Da Mystery of Chessboxin'"
              ]
             }


# get a Json with the existing rapper in the list
existing_resp= requests.get(URL)
pprint(existing_resp.json())

# json.dumps takes a python object and returns it as a JSON string
new_rapper= json.dumps(new_rapper)

# requests.post two paramenters needed -> a url to send the request, a json string to attach to the request
resp= requests.post(URL, json=new_rapper)

# pretty-print the response back from our POST request
pprint(resp.json())
