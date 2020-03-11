from . import seller


@seller.route('/seller/index/')
def index():
    return 'Hello World! This is seller index.'