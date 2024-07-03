import requests
from flask import Flask, render_template, url_for
from flask import request as req 
from dotenv import load_dotenv
import os


app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])

def Index():
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if req.method=="POST":
        load_dotenv('.env')
        api_key = os.getenv('API_KEY')
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": api_key}

        data = req.form["data"]

        min_l = 20
        max_l = int(req.form["maxL"])

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": data,
            "params": {
                "min_length": min_l,
                "max_length": max_l
            },
        })[0]


        return render_template("index.html", result=output["summary_text"])
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.debug=True
    app.run()           # Command used to execute python flask
