from flask import Flask
from flask import render_template
import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/base/')
def base():
    return render_template('base.html')


@app.route('/userinfo/')
def user_info():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    month_first = datetime.datetime(year, month, 1, 0, 0, 0)
    month_first_wek = month_first.weekday()
    
    return render_template('userinfo.html', **locals())


if __name__ == '__main__':
    app.run(port=8026, debug=True)
