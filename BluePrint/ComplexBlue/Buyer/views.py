from Buyer import buyer


@buyer.route('/buyer/')
def index():
    return 'This is buyer index.'
