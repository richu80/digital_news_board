from flask import Blueprint, jsonify, request, session
from models import db, User, Post, Like, Comment
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError

api = Blueprint('api', __name__)

def present_user(user):
    return {
        'id': user.id,
        'username': user.username,
        'phone_number': user.phone_number,
        'role': user.role
    }

def present_post(post):
    likes_count = Like.query.filter_by(post_id=post.id).count()
    user_id = session.get('user_id')
    is_liked_by_current_user = bool(Like.query.filter_by(post_id=post.id, user_id=user_id).first())
    return {
        'id': post.id,
        'user_id': post.user_id,
        'title': post.title,
        'text': post.text,
        'image': post.image,
        'category': post.category,
        'created_at': post.created_at,
        'is_author': user_id == post.user_id,
        'likes_count': likes_count,
        'is_liked': is_liked_by_current_user
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
    if not data or not all(k in data for k in ('username','phone_number','password')):
        return jsonify({"error": "Invalid request"}), 400
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already exists"}), 409
    if User.query.filter_by(phone_number=data['phone_number']).first():
        return jsonify({"error": "Phone number already registered"}), 409
    user = User(username=data['username'], phone_number=data['phone_number'], role='student')
    user.set_password(data['password'])
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500
    return jsonify({"message": "User registered successfully"}), 201

@api.route('/sign_in', methods=['POST'])
def sign_in():
    data = request.get_json()
    if not data or not all(k in data for k in ('phone_number','password')):
        return jsonify({"error": "Invalid request"}), 400
    user = User.query.filter_by(phone_number=data['phone_number']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Invalid credentials"}), 401
    login_user(user)
    session['user_id'] = user.id
    return jsonify({"message": "Login successful"}), 200

@api.route('/logout', methods=['POST'])
def logout():
    logout_user()
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

@api.route('/create_post', methods=['POST'])
@login_required
def create_post():
    data = request.get_json()
    if not data or not all(k in data for k in ('title','category','text')):
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
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([present_post(p) for p in posts]), 200

@api.route('/post/<int:post_id>/delete', methods=['DELETE'])
@login_required
def post_delete(post_id):
    post = Post.query.get_or_404(post_id)
    if session.get('user_id') != post.user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    Comment.query.filter_by(post_id=post.id).delete()
    Like.query.filter_by(post_id=post.id).delete()
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'}), 200


@api.route('/post/<int:post_id>/like', methods=['POST'])
@login_required
def post_like(post_id):
    post = Post.query.get_or_404(post_id)
    if Like.query.filter_by(user_id=session['user_id'], post_id=post_id).first():
        return jsonify({'error': 'Already liked'}), 400
    db.session.add(Like(user_id=session['user_id'], post_id=post_id))
    db.session.commit()
    return jsonify({'message': 'Post liked successfully'}), 200

@api.route('/post/<int:post_id>/unlike', methods=['DELETE'])
@login_required
def post_unlike(post_id):
    like = Like.query.filter_by(user_id=session['user_id'], post_id=post_id).first_or_404()
    db.session.delete(like)
    db.session.commit()
    return jsonify({'message': 'Post unliked successfully'}), 200

@api.route('/get_users', methods=['GET'])
def get_users():
    return jsonify([present_user(u) for u in User.query.all()]), 200

@api.route('/post/<int:post_id>/create_comment', methods=['POST'])
@login_required
def create_comment(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json() or {}
    comment = Comment(post_id=post_id, user_id=session['user_id'], text=data.get('text',''))
    db.session.add(comment)
    db.session.commit()
    return jsonify(present_comment(comment)), 201

@api.route('/post/comment/<int:comment_id>/delete', methods=['DELETE'])
@login_required
def comment_delete(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    if session.get('user_id') != comment.user_id:
        return jsonify({'error': 'Unauthorized'}), 403
    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment deleted successfully'}), 200