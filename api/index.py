# api/index.py
from flask import Flask, jsonify

app = Flask(__name__)

# Define a simple GET endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# For Vercel to recognize the app
# from api.index import app as application
app = app