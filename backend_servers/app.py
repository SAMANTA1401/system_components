from flask import Flask, jsonify
import os

app = Flask(__name__)
server_id = os.environ.get("SERVER_ID", "backend-1")

@app.route('/greet')
def greet():
    return jsonify({"message": f"Hello from {server_id}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)