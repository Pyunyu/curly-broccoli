# This file contains the main application code for the Flask API.

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from models import db, User, Address, Product, Cart, CartItem, Order

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

@api.route("/carts/<int:id>", methods=["GET"])
def get_carts_by(id):
     """
     Get a new carts ID in the database with the provided data.
     """
     search_cart = session.query(Cart).get(id)
     
     return jsonify(search_cart.serialize()), 200
 
@api.route("/carts/<int:id>/items", methods=["POST"])
def add_carts_item(id):
     """
     Adds items to carts in the database with the provided data.
     """
     search_cart = session.query(Cart).get(id)
     data = request.get_json()
     product_id = data.get("product_id")
     search_product = session.query(Product).get(product_id)
     quantity = data.get("quantity")
     new_cart_item = CartItem(quantity=quantity,cart=search_cart,products=search_product)
     session.add(new_cart_item)
     session.commit()
     return jsonify({"message": "Cart has items added successfully"}), 201

@api.route("/carts/<int:id>/items", methods=["DELETE"])
def delete_carts_item(id):
    """
    Delete a carts item in the database with the provide data.
    """
    search_cart_item = session.query(CartItem).get(id)
    session.delete(search_cart_item)
    session.commit()
    return jsonify({"message": "cosito del carrito borrado"}), 201

@api.route("/orders", methods=["POST"])
def create_orders():
     """
     Create a new orders in the database with the provided data.
     """
     data = request.get_json()
     cart_id = data.get("cart_id")
     search_cart = session.query(Cart).get(cart_id)
     total = search_cart.gettotal()
     new_order = Order(total_ammount=total, status="pending", client_info="Stay")
     session.add(new_order)
     session.commit()
     return jsonify({"message": "Order created successfully"}), 201
 
@api.route("/orders", methods=["GET"])
def get_orders():
     """
     Retrieve all orders from the database and return them in JSON format.
     """
     orders = session.query(Order).all()
 
     ordenes_en_formato_diccionario = []
 
     for order in orders:
         order_dict = {
             "id": order.id,
             "client_info": order.client_info,
             "total_ammount": order.total_ammount
             
         }
         ordenes_en_formato_diccionario.append(order_dict)
 
     return jsonify(ordenes_en_formato_diccionario)

@api.route("/orders/<int:id>", methods=["GET"])
def search_single_order_by_(id):
     """
    Search an existing order in the database with the provided data.
     """
     # Step 1: Get the order to update
     order = session.query(Order).get(id)
 
     # Step 2: Check if the order exists
     if not order:
         return jsonify({"message": "Order not found"}), 404
     
     order_dict = {
             "id": order.id,
             "client_info": order.client_info,
             "total_ammount": order.total_ammount,
             "status": order.status
         }
 
     return jsonify(order_dict)
 
@api.route("/orders/<int:id>", methods=["PUT"])
def update_order(id):
     """
     Update an existing order in the database with the provided data.
     """
     # Step 1: Get the order to update
     order_to_update = session.query(Order).get(id)
 
     # Step 2: Check if the order exists
     if not order_to_update:
         return jsonify({"message": "Order not found"}), 404
 
     # Step 3: Get the updated data from the request
     data = request.get_json()
 
     # Step 4: Update the product fields
     if "status" in data:
         order_to_update.status = data["status"]
     
 
     # Step 5: Commit the changes to the database
     session.commit()
 
     # Step 6: Return a success message
     return jsonify({"message": "order updated successfully"}), 200

if __name__ == "__main__":
    api.run(port=5000, debug=True)