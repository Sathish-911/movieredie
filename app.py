from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open("urls.json", "r", encoding="utf-8") as f:
        links = json.load(f)

    return render_template("index.html", links=links)

if __name__ == "__main__":
    app.run(debug=True)