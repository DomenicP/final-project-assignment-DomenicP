"""Simple web server for camera streaming demo."""

__version__ = "0.1.0"

from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
app.config.from_object('web_server.default_settings')
app.config.from_envvar('WEB_SERVER_SETTINGS', silent=True)

sock = Sock(app)

@app.route("/")
def index():
    return render_template("index.html")

@sock.route('/ws')
def socket_handler(ws):
    while True:
        data = ws.receive()
        print(data)
