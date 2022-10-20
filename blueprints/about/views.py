from flask import Blueprint, jsonify

about = Blueprint('about', __name__)

def about_me():
    return "About me"

def about_my_work():
    return jsonify({"status": "UP"}), 200