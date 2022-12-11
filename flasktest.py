#!/bin/python3

from flask import Flask, render_template
import requests
import json 

app = Flask(__name__)

def get_chart():
    url = "https://quickchart.io/chart?c={type:'bar',data:{labels:['Q1','Q2','Q3','Q4'], datasets:[{label:'Users',data:[50,60,70,180]},{label:'Revenue',data:[100,200,300,400]}]}}"

    r = json.loads(requests.request("GET", url).text)
    

@app.route("/")
def index():
    return render_template("index.html")

app.run(host="0.0.0.0", port=80)
