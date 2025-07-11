from flask import Flask

app = Flask(__name__)


@app.route("/info")
def lwinfo():
	return "This Is Sahil Singh"

@app.route("/phone")
def lwphone():
	return "1234567890"

app.run(host="0.0.0.0")
