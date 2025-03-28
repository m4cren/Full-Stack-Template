import eventlet

eventlet.monkey_patch()

from flask import Flask
from .extensions import db, migrate, socketio, jwt
from .db_config import schema, password, username, host
from .error_handler import handle404
from .sockets import SocketIO
import os
import pymysql
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

pymysql.install_as_MySQLdb()


def create_website():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
    app.config["JWT_SECRET_KEY"] = os.getenv('JWT_KEY')
    CORS(app, supports_credentials=True)

  

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{username}:{password}@{host}/{schema}?charset=utf8"
    )
   

    from .api.auth import auth
   
    from .error_handler import error_handler

 
    app.register_blueprint(auth)

    app.register_error_handler(404, handle404)

    # from db_models import 'you tables'

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app, async_mode="eventlet", cors_allowed_origins="*")

    create_database(app)

    return app


def create_database(app):
    
    with app.app_context():
        db.create_all()
