import os


# Comment this out during test
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import Flask, render_template


import json
from flask_sqlalchemy import SQLAlchemy



 
app = Flask(__name__)
CORS(app)

# replace with link to test first 
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)


class shoppingcart(db.Model):
      __tablename__ = 'CART'

      id = db.Column(db.VARCHAR(255), primary_key=True)

      def __init__(self,id):
             self.id = id
    
      def json(self):
            return {"id": self.id}



@app.route("/cartitems")
def get_all():
    cart_items = shoppingcart.query.all()
    if len(cart_items):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "products": [product.json() for product in cart_items]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No items in cart"
        }
    ), 404



@app.route("/add/<string:id>", methods=['POST'])
def addToCart(id):
    
    # data = request.get_json()
    
    ID = shoppingcart(id)
    try:
        db.session.add(ID)
        db.session.commit()
    except:
        return jsonify(
        {
                "code":500,
                "data":{
                    "cart_id":id
                },
                "message":"An error occured while adding to cart."
            }
        ),500
    
    return jsonify(
        {
            "code":201,
            "data":ID.json()
        }
    ),201

 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

 
                