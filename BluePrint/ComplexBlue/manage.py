from flask import Flask
from Buyer import buyer
from Seller import seller
from Manger import manager

app = Flask(__name__)
app.register_blueprint(buyer)
app.register_blueprint(seller)
app.register_blueprint(manager)


if __name__ == '__main__':
    print(app.url_map)
    app.run(port=9080, debug=True)


"""
Map([
    <Rule '/seller/' (GET, HEAD, OPTIONS) -> seller.index>,
    <Rule '/buyer/' (GET, HEAD, OPTIONS) -> buyer.index>,
    <Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>
])
"""