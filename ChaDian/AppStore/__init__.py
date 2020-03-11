import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


pymysql.install_as_MySQLdb()
models = SQLAlchemy()


def create():
    app = Flask(__name__)
    print(__name__)
    app.config.from_object('settings.Config')
    models.init_app(app)  # # models = SQLAlchemy(app) 加载数据库
    from .Buyer import buyer
    from .Seller import seller
    app.register_blueprint(buyer)
    app.register_blueprint(seller)
    return app