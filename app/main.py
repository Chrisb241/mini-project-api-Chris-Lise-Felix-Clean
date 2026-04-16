from flask import Flask, jsonify
import datetime
from app.gcs import read_json_from_gcs

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
@app.route("/data")
def get_data():
    try:
        return jsonify(read_json_from_gcs())
    except Exception as e:
        return jsonify({"error": str(e)})



