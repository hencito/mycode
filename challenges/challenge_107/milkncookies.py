#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import redirect
from flask import url_for

app = Flask(__name__)

# entry point for our users
# renders at template that asks for their name
# login.html point to /setcookie

@app.route("/login")
@app.route("/")
def index():
    return render_template("login.html")

# set cookie and send it back to the user
@app.route("/setcookie", methods = ["POST","GET"])
def setcookie():
    #if user generates aPOST to our API
    if request.method == "POST":
        if request.form.get("nm"):# if nm was assigned via POST
        # if request.form["nm"] <-- this also works, but returns ERROR if no nm
            user = request.form.get("nm") # grab the value of nm from the POST
        else: #if a user sent a post without nm then assign value default user
            user = "defaultuser"

        # note that cookies are set on response objects
        # Since you normally just retuirn strings
        # Flask will convert them into response objects for you.
        resp = make_response(render_template("readcookie.html"))
        # add a cookie to our response object
                        # cookievar #value
        resp.set_cookie("userID",user)


        # return our respose object includes our cookie
        return resp

    if request.method == "GET": # if the user sends a GET
        return redirect(url_for("index")) #redirect to index

# check users cookie for their name
@app.route("/getcookie")
def getcookie():
    # attempt to read the value of userID from user cookie
    name = request.cookies.get("userID") # preferred method

    # name = request.cookies["userID"] # <-- this works but returns error
                                       # if value userID is not in cookie

    # retung HTML embeded with name (value of userID read from cookie)
    return f'<hi> Welcom {name}</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=2224)
