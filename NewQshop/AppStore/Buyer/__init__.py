from flask import Blueprint
from flask_restful import Api

buyer = Blueprint('buyer', __name__)
apibuyer = Api(buyer)

from . import views