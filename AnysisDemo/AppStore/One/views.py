import json
import pymysql


from flask import request
from flask import render_template
from flask_restful import Resource

from . import one


@one.route('/one/index/')
def index():
    return render_template('one/index.html')


@one.route('/one/api/')
def one_api():
    ret = {
        'code': 200,
        'version': 1.0,
        'frame': 'flask 1.1.1',
        'data': [],
    }
    conn = pymysql.connect(host='10.10.14.164',
                           port=33306,
                           user='root',
                           password='123456',
                           db='vuedemo')

    cursor = conn.cursor()
    sql = "select * from class_info;"
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    # print(data)
    ret['data'] = data
    return ret
