"""Simple web server for camera streaming demo."""

__version__ = "0.1.0"

import json
import logging

import zmq
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
app.config.from_object('web_server.default_settings')
app.config.from_envvar('WEB_SERVER_SETTINGS', silent=True)

web_sock = Sock(app)

zmq_context = zmq.Context()
zmq_sock = zmq_context.socket(zmq.PUB)
zmq_sock.connect("tcp://localhost:5555")

@app.route("/")
def index():
    return render_template("index.html")

@web_sock.route('/ws')
def socket_handler(ws):
    while True:
        msg = json.loads(ws.receive())
        app.logger.info(f"Received message {msg}")
        zmq_sock.send_string(f"{msg['topic']} {json.dumps(msg['value'])}")

if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
