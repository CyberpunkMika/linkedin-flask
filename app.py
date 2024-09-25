import json
import os.path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/your-url", methods=["GET", "POST"])
def yoururl():
    if request.method == "POST":
        urls = {}

        if os.path.exists("urls.json"):
            with open("urls.json") as url_file:
                urls = json.load(url_file)

        if request.form["code"] in urls.keys():
            return redirect(url_for("home"))

        urls[request.form["code"]] = {"url": request.form["url"]}
        with open("urls.json", "w") as url_file:
            json.dump(urls, url_file)
        return render_template("your_url.html", code=request.form["code"])
    return redirect(url_for("home"))
