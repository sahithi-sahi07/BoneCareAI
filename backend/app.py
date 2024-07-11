from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    
    # Dummy prediction logic
    dummy_prediction = "This is a dummy prediction result."
    
    return jsonify({'prediction': dummy_prediction})

if __name__ == '__main__':
    app.run(debug=True)
