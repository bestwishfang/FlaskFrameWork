from flask import Flask

app = Flask(__name__)


@app.route('/')
def new():
    # 啊 = 1 / 0
    return "日天"


@app.route('/index/')
def index():
    return "BUG yi dui ..."


def register():
    pass


def login():
    pass


if __name__ == '__main__':
    app.run(port=8099,debug=True)
