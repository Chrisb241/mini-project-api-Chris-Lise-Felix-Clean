from flask import Flask, jsonify, request
import datetime
from app.gcs import read_json_from_gcs, write_to_gcs

app = Flask(__name__)

# HELLO
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello"})

# STATUS
@app.route("/status", methods=["GET"])
def status():
    return jsonify({"date": str(datetime.datetime.now())})

# DATA
@app.route("/data", methods=["POST"])
def add_data():
    body = request.get_json()
    if not body:
        return jsonify({"error": "Corps JSON manquant"}), 400
    write_to_gcs(body)
    return jsonify({"message": "Entrée ajoutée avec succès"}), 201



