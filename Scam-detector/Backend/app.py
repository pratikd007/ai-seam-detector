from flask import Flask, request, jsonify
from flask_cors import CORS
from model import detect_scam

app = Flask(__name__)
CORS(app)

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    text = data.get("message", "")
    result = detect_scam(text)
    return jsonify(result)

if __name__ == '__main__':
    print("Starting Flask server...")   # 👈 add this line
    app.run(debug=True)