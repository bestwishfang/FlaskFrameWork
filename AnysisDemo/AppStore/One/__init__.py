from flask import Blueprint
from flask_restful import Api

one = Blueprint('one', __name__)
apione = Api(one)

from . import views