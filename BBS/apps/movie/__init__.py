from flask import Blueprint
from flask_restful import Api

movie = Blueprint('movie', __name__, url_prefix='/movie')
apimovie = Api(movie)

from . import views
