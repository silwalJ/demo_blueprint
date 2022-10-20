from flask import Blueprint, jsonify

product = Blueprint('product', __name__)

def list_of_clothes():
    return "List of clothes"

def list_of_shoes():
    return "List of shoes"

def list_of_tshirts():
    return jsonify({"status": "UP"}), 200