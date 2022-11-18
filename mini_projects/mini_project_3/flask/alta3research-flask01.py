#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import jsonify

app = Flask(__name__)

mgsCharacters =[
    {
    "name": "David",  
    "codeName": "Solid Snake",
    "association": ["FOXHOUND", "Les Enfants Terribles","Green Beret"],
    "quote": "Life isn't just about passing on your genes. We can leave behind much more than just DNA. Through speech, music, literature and movies... what we've seen, heard, felt ...anger, joy and sorrow... these are the things I will pass on. That's what I live for. ―Solid Snake",
    "occupation": "Mercenary"
    },
    {
    "name": "John",  
    "codeName": "Big Boss",
    "association": ["FOXHOUND", "Militaires Sans Frontières","The Patriots","La-li-lu-le-lo", "Cipher"],
    "quote": "We have no nation, no philosophy, no ideology. We go where we're needed, fighting not for country, not for government, but for ourselves. We need no reason to fight. We fight because we are needed. We will be the deterrent for those with no other recourse. We are soldiers without borders, our purpose defined by the era we live in.―Big Boss",
    "occupation": "Mercenary"},

    {
    "name": "N/A",  
    "codeName": "The Boss",
    "association": ["Cobra Unit", "The Philosophers","FOX","SAS", "CIA", "NASA", "GRU"],
    "quote": "Is there such a thing as an absolute, timeless enemy? There is no such thing, and never has been. And the reason is that our enemies are human beings like us. They can only be our enemies in relative terms. The world must be made whole again. ―The Boss",
    "occupation": "Mercenary"}          
             ]


# standard route, that is without "authentication"; this term is used loosely
@app.route("/")
def index():
    # render the jinja template "hellouser.html"
    # this is the basic hello page
    return render_template("hellouser.html")

# invalid agent route, that is without "authentication"; this term is used loosely
@app.route("/agent")
def invalidagent():
    # render the jinja template "hellouser.html"
    # this is the basic hello page
    return render_template("hellouser.html")   

# valid user/agent route
@app.route("/agent/<codeName>")
def valid(codeName):
    # render the jinja template "hellouser.html"
    # apply the value of username for the var name
    #for char in mgsCharacters:

    # print("Hello",mgsCharacters)

        #name = char["name"]

    return render_template("hellouser.html", codeName=codeName, mgsCharacters=mgsCharacters)


#returns a json with the list of characters
@app.route("/characters")
def characters():


    return jsonify(mgsCharacters)



if __name__ =="__main__":
    app.run(host="0.0.0.0", port = 2224)
