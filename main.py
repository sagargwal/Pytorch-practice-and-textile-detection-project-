from flask import Flask, request, jsonify
from torch_utils import transform_image, get_prediction

app = Flask(__name__)

# Allowed extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        file = request.files.get('file')

        if file is None or file.filename == "":
            return jsonify({"error": "No file provided"}), 400

        if not allowed_file(file.filename):
            return jsonify({"error": "File format not supported. Please use png, jpg, or jpeg."}), 400

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            class_idx, class_name = get_prediction(tensor)
            return jsonify({
                "prediction_index": class_idx.item(),
                "class_name": class_name
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
