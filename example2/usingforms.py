from flask import Flask, send_from_directory, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def main():
    return send_from_directory("html", "index.html")

@app.route("/css/<path>", methods = ["GET"])
def serve_css(path):
    return send_from_directory("css", path)

@app.route("/submit", methods = ["POST"])
def handle_form():
	user = request.form["username"]
	password = request.form["password"]
	
	return "the login data was: <b>{}:{}</b>".format(user, password)

app.run()