from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def main():
    return send_from_directory("html", "main.html")

@app.route("/css/<path>", methods = ["GET"])
def serve_css(path):
    return send_from_directory("css", path)

app.run()