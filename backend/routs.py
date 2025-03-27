from flask import Blueprint, jsonify, request, session, redirect, url_for, flash
from models import db, User, Post, Like


api = Blueprint('api', __name__)



def present_user(user):
    return {
        'id': user.id,
        'username': user.username,
        'phone_number': user.phone_number,
        'role': user.role
    }



def present_post(post):
    return {
        'id': post.id,
        'user_id': post.user_id,
        'title': post.title,
        'text': post.text,
        'image': post.image,
        'category': post.category,
        'created_at': post.created_at
    }



@api.route('/sign_up', methods=['POST'])
def sign_up():
    data = request.get_json()

    if not data or not all(key in data for key in ['username', 'phone_number', 'password']):
        return jsonify({"error": "Invalid request"}), 400

    user = User(
        username=data['username'],
        phone_number=data['phone_number'],
        role='student'
    )
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201



@api.route('/sign_in', methods=['POST'])
def sign_in():
    data = request.get_json()

    if not data or not all(key in data for key in ['phone_number', 'password']):
        return jsonify({"error": "Invalid request"}), 400

    user = User.query.filter_by(phone_number=data['phone_number']).first()

    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Invalid phone number or password"}), 401

    session['user_id'] = user.id
    flash("Login successful.", "success")

    return jsonify({"message": "Login successful"}), 200



@api.route('/create_post', methods=['POST'])
def create_post():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()

    if not data or not all(key in data for key in ['title', 'category', 'text']):
        return jsonify({"error": "Invalid request"}), 400

    post = Post(
        user_id=session['user_id'],
        title=data['title'],
        category=data['category'],
        text=data['text'],
        image=data.get('image')
    )

    db.session.add(post)
    db.session.commit()

    return jsonify(present_post(post)), 201