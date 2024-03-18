import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"


@app.route("/nga")
def nga():
    return ("<h1>Привет, нига!</h1>"
            "<h2>Я за тобой наблюдаю!</h2>")



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
