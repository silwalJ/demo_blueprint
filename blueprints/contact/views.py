from flask import Blueprint, jsonify

contact = Blueprint('contact', __name__)

def contact_me():
    return "Contact Me"

def contact_for_sponsor():
    return jsonify({"status": "UP"}), 200