from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('web_server.default_settings')
app.config.from_envvar('WEB_SERVER_SETTINGS', silent=True)

@app.route("/")
def index():
    return render_template("index.html")
