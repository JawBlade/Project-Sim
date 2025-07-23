from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/healthz')
def healthz():
    return "OK", 200


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
