from flask import Flask, send_from_directory, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def main():
    return send_from_directory("html", "index.html")

@app.route("/css/<path>", methods = ["GET"])
def serve_css(path):
    return send_from_directory("css", path)

@app.route("/upload-file", methods = ["POST"])
def handle_form():
    # here we get a File object
    file = request.files["file"]

    # and we read its contents with the read() method
    contents = file.read()
    return str(contents)

app.run()