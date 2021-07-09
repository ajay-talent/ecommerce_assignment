from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../ecommerce_assignment/data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    firstName = db.Column(db.String(30), nullable=False)
    lastName = db.Column(db.String(30), nullable=False)
    address1 = db.Column(db.String(30), unique=False, nullable=False)
    address2 = db.Column(db.String(30), unique=False, nullable=False)
    city = db.Column(db.String(30), unique=False, nullable=False)
    state = db.Column(db.String(30), unique=False, nullable=False)
    country = db.Column(db.String(30), unique=False, nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.BigInteger, nullable=False)
    cart_ref = db.relationship('Cart', backref='user_ref')


class Categories(db.Model):
    categoryId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    product_ref = db.relationship('Product', backref='cate_ref')


class Products(db.Model):
    productId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    image = db.Column(db.String(50), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    categoryId = db.Column(db.Integer, db.ForeignKey('categories.categoryId'), nullable=False, unique=True)
    cart_ref = db.relationship('Cart', backref='products_ref')
    sales_ref = db.relationship('SalesTransaction', backref='product_ref')


class Cart(db.Model):
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False, unique=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.productId'), nullable=False, unique=True)


class SalesTransaction(db.Model):
    transactionId = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.productId'), nullable=False, unique=True)
    transaction_date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    ac_number = db.Column(db.BigInteger, nullable=False)
    cvv = db.Column(db.Integer, nullable=False)


db.create_all()