from flask import Flask
from flask_cors import CORS
from models import init_db
from routes import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.secret_key="24"
init_db(app)
CORS(app, supports_credentials=True)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)