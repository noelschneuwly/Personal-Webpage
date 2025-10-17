from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/articles", methods=["GET"])
def articles():
    return render_template("articles.html")

@app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=False)