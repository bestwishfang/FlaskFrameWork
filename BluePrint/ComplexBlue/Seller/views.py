from Seller import seller


@seller.route('/seller/')
def index():
    return 'This is Seller index.'

