from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/skjema", methods = ["GET", "POST"])
def skjema():
    if request.method == "POST":
        navn = request.form["navn"]

        return render_template("svar.html", navn = navn)
    return render_template("skjema.html")