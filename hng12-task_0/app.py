from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

@app.route('/', methods=['GET'])
def get_info():
    """Returns JSON with email, current datetime, and GitHub repo URL."""
    response = {
        "email": "adetokunadenike@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/AdetokunAdenike/HNG12-INTERNSHIP.git"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
