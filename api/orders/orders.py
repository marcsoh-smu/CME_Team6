import os

SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']

from flask import Flask, request, jsonify
from flask_cors import CORS


import json
from flask_sqlalchemy import SQLAlchemy

 
app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=True)
