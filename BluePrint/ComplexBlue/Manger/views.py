from Manger import manager


@manager.route('/manager/')
def index():
    return 'This is Manger index.'
