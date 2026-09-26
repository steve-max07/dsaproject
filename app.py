from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)

# UPDATED: Enforce standard headers and allow preflight check requests
CORS(app, resources={r"/*": {
    "origins": "*",
    "methods": ["POST", "GET", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"]
}})

# ADDED: Home route so Render's system health checks pass with a 200 OK 
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "healthy", "message": "Backend server is running smoothly!"}), 200

@app.route('/api/reverseword', methods=['POST'])
def reverse_word():
    try:
        data = request.get_json()
        
        # Guard clause against empty payloads
        if not data:
            return jsonify({"reversedText": "Backend Error: No data received"}), 400
            
        user_word = data.get('text', '')

        # Using explicit shell=False array execution for Linux compatibility
        result = subprocess.run(['./reverseword', user_word], capture_output=True, text=True, check=True)
        return jsonify({"reversedText": result.stdout.strip()})
        
    except subprocess.CalledProcessError as e:
        # Catch specific failures from the C binary run
        return jsonify({"reversedText": f"C Binary Error: {e.stderr.strip() if e.stderr else 'Execution failed'}"}), 500
    except Exception as e:
        # If the server routing or other logic fails, catch it here
        return jsonify({"reversedText": f"Backend Error: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
