from flask import Flask, jsonify
import datetime
from app.gcs import read_json_from_gcs
import google.generativeai as genai
import os

app = Flask(__name__)

# Config Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# HELLO
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello"})

# STATUS
@app.route("/status", methods=["GET"])
def status():
    return jsonify({"date": str(datetime.datetime.now())})

# DATA
@app.route("/data")
def get_data():
    try:
        return jsonify(read_json_from_gcs())
    except Exception as e:
        return jsonify({"error": str(e)})

# POEM
@app.route("/poem", methods=["GET"])
def generate_poem():
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            "Écris un court poème original sur la programmation, en français, de 4 vers."
        )
        return jsonify({
            "status": "success",
            "poem": response.text
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
