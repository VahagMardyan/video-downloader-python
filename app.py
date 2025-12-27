from flask import Flask, render_template, request, jsonify
from core import download_media

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("video-url")
    fmt = request.form.get("format","mp4")
    message, success = download_media(url, fmt)
    return jsonify({
        "success" : success,
        "message" : message
    })

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

