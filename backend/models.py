from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    hash_password = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(12), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    def set_password(self, password):
        self.hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.hash_password, password)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
    title = db.Column(db.String(70), nullable=False)
    text = db.Column(db.Text)
    image = db.Column(db.String(200))
    category = db.Column(db.String(25), nullable=False)
    posts_time = db.Column(db.DateTime, default=db.func.current_timestamp())


class likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("Posts.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)




def init_db(app):
    db.init_app(app)
    bcrypt.init_app(app)
    Migrate(app, db)