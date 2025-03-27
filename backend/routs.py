from flask import Blueprint, jsonify, request, send_file
from models import db, Users, Posts, likes

api = Blueprint('api', __name__)

def return_user(user):
    return {'id': user.id, 
            'username': user.username, 
            'phone_number': user.phone_number, 
            'role': user.role
    }

def return_posts(post):
    return {'id': post.id, 
            'user_id': post.user_id, 
            'title': post.title, 
            'text': post.text, 
            'image': post.image, 
            'category': post.category, 
            'posts_time': post.posts_time
    }

@api.route('/sign_up', methods=['POST'])
def sign_up():
    user = Users(username = request.form['username'], 
                phone_number = request.form['phone_number'], 
                password = request.form['password'],
                role = 'student'
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("sign_in"))


@api.route('/sign_in', methods=['POST'])
def sign_in():
    data = request.get_json()
    phone_number = request.form['phone_number']
    password = request.form['password']
    user = User.query.filter_by(phone_number=phone_number).first()
    if user or not user.check_password(data['password']):
        session['user_id'] = user.id
        flash("Login complete.", "success")
        print("1234")
        return redirect(url_for("posts"))
    

@api.route('/create_post', methods=['POST'])
def create_post():
    post = Posts(title = request.form['title'],
                 category = request.form['category'],
                 text = request.form['text'],
                 #разобраться с изображением
    )
    db.session.add(post)
    db.session.commit()
    return redirect(url_for("home"))



