from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

# baseDir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/jpbadan/Desktop/AerospaceExpress/tmp/test.db'
db = SQLAlchemy(app)


from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/')

from app.api.user import bp as user_bp
app.register_blueprint(user_bp, url_prefix='/user')

from app.api.post import bp as post_bp
app.register_blueprint(post_bp, url_prefix='/post')
