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

class orders(db.Model):
      __tablename__ = 'ORDERS'

      id = db.Column(db.VARCHAR(255), primary_key=True)

      def __init__(self,id):
             self.id = id
    
      def json(self):
            return {"id": self.id}

@app.route("/ordersitem")
def get_all():
    orders_items = orders.query.all()
   
    if len(orders_items):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "products": [product.json() for product in orders_items]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No items in orders"
        }
    ), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5010, debug=True)