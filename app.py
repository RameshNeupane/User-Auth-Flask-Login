from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# init SQLAlchemy so we can use is later in our models
db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  
  app.config['SECRET_KEY'] = 'laskdfqdkfja2343423LKJDFQ3Q45'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "db.sqlite")}'
  
  db.init_app(app)
  
  login_mamager = LoginManager()
  login_mamager.login_view = 'auth.login'
  login_mamager.init_app(app)
  
  from project.models import User
  
  @login_mamager.user_loader
  def load_user(user_id):
    # since the user_id is just the primary key of our user table,
    # use it in the query for the user
    return User.query.get(int(user_id))
  
  # blueprint for auth routes in our app
  from project.auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)
  
  # blueprint for non-auth parts of app
  from project.main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  return app