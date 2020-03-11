import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATICFILES_DIR = os.path.join(BASE_DIR, 'AppStore/static')


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@10.10.14.164:33306/vuedemo"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True



class RunConfig(Config):
    DEBUG = True