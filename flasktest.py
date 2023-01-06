#!/usr/bin/python3

from flask import Flask, render_template
import requests
import json 
import sqlalchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    email = None
    return render_template("login.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    return render_template("signup.html")

@app.route("/visualise")
def visualisation():
    return render_template("visualisation.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
