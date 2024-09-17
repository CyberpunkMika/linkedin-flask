from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/your-url", methods=["GET", "POST"])
def yoururl():
    if request.method == "POST":
        return render_template("your_url.html", code=request.form["code"])
    else:
        return "This is not valid"
