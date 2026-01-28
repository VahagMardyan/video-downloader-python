from flask import Flask, render_template, request, send_file
from core import download_media
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("video-url")
    fmt = request.form.get("format", "mp4")
    
    message, success, file_path = download_media(url, fmt)
    
    if success and os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return f"Error: {message}", 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)