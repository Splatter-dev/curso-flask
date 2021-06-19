from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    print(__name__)
    return "<h1>Hello, Codeshow - curso</h1>"


@app.route("/sobre")
def sobre():
    # 1 / 0
    return f"<p>este é o melhor site de delivery</p>"
