#!/usr/bin/python3

from flask import Flask, redirect, url_for, render_template, request, session, flash
import requests
import json 
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK-MODIFICATIONS"]  = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["fname"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first() 
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("profile.html", user = user)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("You have been logged out!", "info")
    return redirect(url_for("login"))

@app.route("/signup", methods=["POST", "GET"])
def signup():

    return render_template("signup.html")

@app.route("/visualise")
def visualisation():
    return render_template("visualisation.html")

if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True, host="0.0.0.0", port=80)
