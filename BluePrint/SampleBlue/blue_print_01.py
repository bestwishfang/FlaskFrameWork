from flask import Blueprint

simple_01 = Blueprint('simple_page_01', __name__)


@simple_01.route('/01/')
def index():
    return 'Hello World! This is simple_01.'
