# This file contains the main application code for the Flask API.

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from models import db, User, Address, Product, Cart

from flask import Flask, request, jsonify
from addreses import address_api
from session import session

# Create a new Flask application
api = Flask(__name__)
# Register the address_api blueprint
api.register_blueprint(address_api)


@api.route("/users", methods=["GET"])
def get_users():
    """
    Retrieve all users from the database and return them in JSON format.
    """
    users = session.query(User).all()

    usuarios_en_formato_diccionario = []

    for user in users:
        user_dict = {
            "id": user.id,
            "name": user.name,
            "fullname": user.fullname,
            "nickname": user.nickname,
        }
        usuarios_en_formato_diccionario.append(user_dict)

    return jsonify(usuarios_en_formato_diccionario)

@api.route("/users", methods=["POST"])
def create_user():
    """
    Create a new user in the database with the provided data.
    """
    data = request.get_json()
    new_user = User(name=data["name"], fullname=data["fullname"], nickname=data["nickname"])
    session.add(new_user)
    session.commit()
    return jsonify({"message": "User created successfully"}), 201

@api.route("/product", methods=["POST"])
def create_product():
    """
    Create a new user in the database with the provided data.
    """
    data = request.get_json()
    new_product = Product(product=data["product"], price=data["price"], description=data["description"], stock=data["stock"], straykidsmember=data["straykidsmember"], color=data["color"])
    session.add(new_product)
    session.commit()
    return jsonify({"message": "Product created successfully"}), 201

@api.route("/product", methods=["GET"])
def get_product():
    """
    Retrieve all users from the database and return them in JSON format.
    """
    product = session.query(Product).all()

    cositos_en_formato_diccionario = []

    for product in product:
        product_dict = {
            "id": product.id,
            "product": product.product,
            "price": product.price,
            "description": product.description,
            "stock": product.stock,
            "straykidsmember": product.straykidsmember,
            "color": product.color,
        }
        cositos_en_formato_diccionario.append(product_dict)

    return jsonify(cositos_en_formato_diccionario)


@api.route("/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    """
    Delete a product in the database with the provide data.
    """
    search_product = session.query(Product).get(id)
    session.delete(search_product)
    session.commit()
    return jsonify({"message": "cosito borrado"}), 201

@api.route("/cart", methods=["GET"])
def get_cart():
    """
    Retrieve all  from the database and return them in JSON format.
    """
    cart = session.query(Cart).all()

    carrito_en_formato_diccionario = []

    for cart in cart:
        cart_dict = {
            "id": cart.id,
            "creationdate": cart.creation_date,
        }
        carrito_en_formato_diccionario.append(cart_dict)

    return jsonify(carrito_en_formato_diccionario)

@api.route("/cart", methods=["POST"])
def create_cart():
    """
    Create a new cart in the database with the provided data.
    """
    data = request.get_json()
    new_cart = Cart()
    session.add(new_cart)
    session.commit()
    return jsonify({"message": "Cart created successfully"}), 201

if __name__ == "__main__":
    api.run(port=5000, debug=True)