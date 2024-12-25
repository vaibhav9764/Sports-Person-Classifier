from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)  # Enable CORS support


@app.route('/classify_image', methods=['POST'])
def classify_image():
    # Get the image data from the request
    image_data = request.form.get('image_data')
    if not image_data:
        return jsonify({'error': 'No image data provided'}), 400

    try:
        # Call util function to classify the image
        response_data = util.classify_image(image_data)
        return jsonify(response_data)
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()  # Ensure this function initializes without issues
    app.run(host='0.0.0.0', port=5000)
