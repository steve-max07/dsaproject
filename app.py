from flask import Flask, request, jsonify
from flask_cors import CORS

import subprocess

app = Flask(__name__)
CORS(app) # Connects safely with your simple HTML file

@app.route('/api/reverseword', methods=['POST'])
def reverse_word():
    data = request.get_json()
    user_word = data.get('text', '')

    # Runs your compiled C binary file locally behind the scenes
    # (Make sure you ran: gcc reverse.c -o reverse first)
    result = subprocess.run(['./reverseword', user_word], capture_output=True, text=True)

    return jsonify({"reversedText": result.stdout})

if __name__ == '__main__':
    app.run(port=5000)
