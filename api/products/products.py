import os


# SQLALCHEMY_DATABASE_URI = os.environ['DB_URL']
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']

from flask import Flask, request, jsonify
from flask_cors import CORS

#from secrets_manager import get_secret

import json
from flask_sqlalchemy import SQLAlchemy

 
app = Flask(__name__)
CORS(app)

#db_config = get_secret()

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f'mysql+mysqlconnector://{db_config["username"]}:' +
#     f'{db_config["password"]}@' +
#     f'{db_config["host"]}:3306/' +
#     f'{db_config["db_name"]}'
# )

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)

class Product(db.Model):
    __tablename__ = 'PRODUCT'
 
    id = db.Column(db.String(13), primary_key=True)
    product_name = db.Column(db.String(64), nullable=False)
    price = db.Column(db.String(13), nullable=False)
    description = db.Column(db.String(128))
 
    def __init__(self, name, price, description):
        self.id = id
        self.product_name = product_name
        self.price = price
        self.description = description
 
    def json(self):
        return {"id": self.id, "name": self.product_name, "price": self.price, "description": self.description}

@app.route("/product")
def get_all():
    product_list = Product.query.all()
    if len(product_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "products": [product.json() for product in product_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no books."
        }
    ), 404


@app.route("/product/<string:id>")
def find_by_id(id):
    product = Product.query.filter_by(id=id).first()
    if product:
        return jsonify(
            {
                "code": 200,
                "data": product.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Product not found."
        }
    ), 404




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)

 
                