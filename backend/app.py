from flask import Flask, request, render_template
from model.caption_model import extract_features, generate_caption
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "No image uploaded."
        file = request.files["image"]
        if file.filename == "":
            return "No selected image."
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)
        photo = extract_features(path)
        caption = generate_caption(photo)
        return render_template("index.html", image=file.filename, caption=caption)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
