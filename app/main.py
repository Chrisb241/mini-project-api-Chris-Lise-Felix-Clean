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
    return jsonify({"message": "Entrée ajoutée avec succès"}), 201

# POEM
@app.route("/poem", methods=["GET"])
def poem():
    try:
        vertexai.init(
            project=os.environ.get("GCP_PROJECT_ID"),
            location=os.environ.get("GCP_LOCATION", "europe-west1")
        )
        model = GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            "Écris un court poème original sur la programmation, en français, de 4 vers."
        )
        return jsonify({"status": "success", "poem": response.text}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))