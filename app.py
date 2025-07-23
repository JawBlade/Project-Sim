from flask import Flask

app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
