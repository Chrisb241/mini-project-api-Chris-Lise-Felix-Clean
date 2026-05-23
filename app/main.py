from flask import Flask, jsonify, request
import datetime
import os
import vertexai
from vertexai.generative_models import GenerativeModel
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

# GET DATA
@app.route("/data", methods=["GET"])
def get_data():
    try:
        return jsonify(read_json_from_gcs())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST DATA
@app.route("/data", methods=["POST"])
def add_data():
    body = request.get_json()
    if not body:
        return jsonify({"error": "Corps JSON manquant"}), 400
    write_to_gcs(body)
    return jsonify({"message": "Entrée ajoutée avec succès"}),
    
