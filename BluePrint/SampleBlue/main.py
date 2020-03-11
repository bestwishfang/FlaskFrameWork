from flask import Flask
from blue_print_01 import simple_01
from blue_print_02 import simple_02

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(simple_01)
    app.register_blueprint(simple_02)
    app.run(port=8090, debug=True)
