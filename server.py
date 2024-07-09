from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# Хранилище объектов
objects = []

@app.route('/update_objects', methods=['POST'])
def update_objects():
    global objects
    objects = request.json['objects']
    for obj in objects:
        obj['last_updated'] = time.time()
    return jsonify({"status": "success"}), 200

@app.route('/get_objects', methods=['GET'])
def get_objects():
    return jsonify(objects), 200

if __name__ == '__main__':
    app.run(debug=True)
