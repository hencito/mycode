from flask import Flask
from flask import redirect
from flask import request
from flask import render_template


app = Flask(__name__)

trivia_answers = [{
    "What is 1+1?": 2
}]


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        data = request.json
        if data:

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2224)