from dataclasses import dataclass
from os import abort

import requests
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

from producer import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)
db = SQLAlchemy(app)


@dataclass
class Product(db.Model):
    query = None
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://host.docker.internal:8000/api/user')
    json = req.json()

    try:
        product_user = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(product_user)
        db.session.commit()

        publish('product_liked',id)
    except:
        abort(400, "Your alredy liked this product")

    return jsonify({
        'message': "success"
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
