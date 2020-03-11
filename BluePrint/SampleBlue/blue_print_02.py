from flask import Blueprint

simple_02 = Blueprint('simple_page_02', __name__)


@simple_02.route('/02/')
def index():
    return 'Hello World! This is simple_02.'
