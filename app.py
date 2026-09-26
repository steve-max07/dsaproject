from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)

# Force CORS to allow your GitHub Pages origin explicitly
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/reverse', methods=['POST'])
def reverse_word():
    try:
        data = request.get_json()
        user_word = data.get('text', '')

        # Using explicit shell=False array execution for Linux compatibility
        result = subprocess.run(['./reverseword', user_word], capture_output=True, text=True, check=True)
        return jsonify({"reversedText": result.stdout.strip()})
        
    except Exception as e:
        # If the C program execution fails, send the error back to the browser safely
        return jsonify({"reversedText": f"Backend Error: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
