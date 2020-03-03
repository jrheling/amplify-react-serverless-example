# app.py
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/test")
def hello():
    return "You must have authenticated correctly."

