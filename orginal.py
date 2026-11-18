from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/meny")
def meny():
    return render_template("meny.html")

@app.route("/bestill", methods=["POST", "GET"])
def bestill():
    if request.method == "POST":
        navn = request.form["navn"]
        telefonnummer = request.form["fon"]
        klokkeslett = request.form["Klokkeslett"]
        return render_template("resultat.html", 
                               navn=navn,
                               telefonnummer = telefonnummer,
                               klokkeslett = klokkeslett
                               )

    return render_template("bestill.html")

@app.route("/om")
def om():
    return render_template("om.html")