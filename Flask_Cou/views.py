from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/birthday/<birthday>')
def birthday_trans(birthday):
    """
    :param birthday: 输入生日格式2019-4-5
    :return:
    """
    bir_list= birthday.split('-')
    bir_month = int(bir_list[1])
    bir_day = int(bir_list[2])

    year = datetime.datetime.now().year
    start = datetime.datetime(year, 1, 1, 0, 0, 0).timestamp()
    bir = datetime.datetime(year, bir_month, bir_day, 0, 0, 0).timestamp()
    date = int((bir - start) // (3600 * 24)) + 1
    return "\033[1;34m您的生日是今年的第{}天\033[0m".format(date)


if __name__ == '__main__':
    app.run(debug=True)

