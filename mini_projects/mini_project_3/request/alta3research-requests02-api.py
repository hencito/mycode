#!/usr/bin/env python3
""" Mini_Project_2 Requests - WuTang Style
    In this project I have built an API for 
    WuTang Clan Rappers (really any rapper). I have instantiated the API
    with a single JSON entry.

    Accompanying this api is a python scrip for adding a
    new rapper.

"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import json

app= Flask(__name__)

rapperdata= [{
    "name": "Russell Tyrone Jones",  
    "stageName": "Ol Dirty Bastard",
    "aka": "O.D.B",
    "association": "Wu-Tang Clan",
    "knownFor": "Method Man: 'Ol' Dirty Bastard's name was also a reference to the unique nature of his rapping and, specifically, the fact 'there ain't no father to his style.'",
    "occupation": "Rapper/Songwriter",
    "hits": [
        "Shimmy Shimmy Ya",
        "Got Yourt Money",
        "Ghetto Supastar(That is What You Are)",
        "Da Mystery of Chessboxin'"
              ]
             }]

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           name = data["name"]
           stageName = data["stageName"]
           aka = data["aka"]
           association = data["association"]
           knownFor = data["knownFor"]
           occupation = data["occupation"]
           hits = data["hits"]
           rapperdata.append({"name":name,"stageName":stageName,"aka":aka,"association":association,"knownFor":knownFor,"occupation":occupation,"hits":hits})

    return jsonify(rapperdata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)