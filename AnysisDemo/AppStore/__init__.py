import pymysql
from flask import  Flask
from flask_sqlalchemy import SQLAlchemy


pymysql.install_as_MySQLdb()
models = SQLAlchemy()


def create():
    app = Flask(__name__)
    print(__name__)
    app.config.from_object('settings.Config')
    models.init_app(app)  # models = SQLAlchemy(app)  加载数据库

    from .One import one
    app.register_blueprint(one)
    return app



