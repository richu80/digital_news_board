from flask import Blueprint, jsonify, request, session, redirect, url_for, flash
from models import db, User, Post, Like, Comment
from flask_login import current_user


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
        'created_at': post.created_at,
        'is_author': current_user.is_authenticated and current_user.id == post.user_id
    }


def present_comment(comment):
    return {
        'id': comment.id,
        'post_id': comment.post_id,
        'user_id': comment.user_id,
        'text': comment.text,
        'created_at': comment.created_at
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



@api.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)

    return jsonify({'message': 'Logout successful'}), 200



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



@api.route('/home', methods=['GET'])
def home():
    posts = Post.query.all()

    return jsonify([present_post(post) for post in posts]), 200



@api.route('/post/<int:post_id>', methods=['GET'])
def post(post_id):
    post = Post.query.get(post_id)

    return jsonify(present_post(post)), 200



@api.route('/post/<int:post_id>/delete', methods=['DELETE'])
def post_delete(post_id):
    if 'user_id' not in session:
        return jsonify({'error': "Unauthorized"}), 401
    
    post = Post.query.get(post_id)

    if session['user_id'] != post.user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    if not post:
        return jsonify({'error': 'post not found'}), 404

    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'}), 200


@api.route('/post/<int:post_id>/like', methods=['POST'])
def post_like(post_id):
    if 'user_id' not in session:
        return jsonify({'error': "Unauthorized"}), 401
    
    post = Post.query.get(post_id)

    if not post:
        return jsonify({'error': 'post not found'}), 404
    
    like = Like.query.filter_by(user_id=session['user_id'], post_id=post_id).first()
    
    if like:
        return jsonify({'error': 'You already liked this post'}), 400
    
    like = Like(post_id=post_id,
                user_id=session['user_id']
    )

    db.session.add(like)
    db.session.commit()
    return jsonify({'message': 'Post liked successfully'}), 200



@api.route('/post/<int:post_id>/unlike', methods=['DELETE'])
def post_unlike(post_id):
    if 'user_id' not in session:
        return jsonify({'error': "Unauthorized"}), 401
    
    post = Post.query.get(post_id)

    if not post:
        return jsonify({'error': 'post not found'}), 404
    
    like = Like.query.filter_by(user_id=session['user_id'], post_id=post_id).first()

    if not like:
        return jsonify({'error': 'like not found'}), 400
    
    db.session.delete(like)
    db.session.commit()
    return jsonify({'message': 'Post liked successfully'}), 200


@api.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()

    return jsonify([present_user(user) for user in users]), 200



@api.route('/post/<int:post_id>/create_comment', methods=['POST'])
def create_comment(post_id):
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    post = Post.query.get(post_id)

    if not post:
        return jsonify({'error': 'post not found'}), 404
    
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid request"}), 400
    
    comment = Comment(
        post_id=post_id,
        user_id=session['user_id'],
        text=data['text']
    )

    db.session.add(comment)
    db.session.commit()

    return jsonify(present_comment(comment)), 201



@api.route('/post/comment/<int:comment_id>/delete', methods=['DELETE'])
def comment_delete(comment_id):
    if 'user_id' not in session:
        return jsonify({'error': "Unauthorized"}), 401
    
    comment = Comment.query.get(comment_id)
    if session['user_id'] != comment.user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    if not comment:
        return jsonify({'error': 'comment not found'}), 404
    if session['user_id'] != comment.user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(comment)
    db.session.commit()

