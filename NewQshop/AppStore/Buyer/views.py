import time
import json
import datetime

from flask import request
from flask import render_template
from flask_restful import Resource

from . import buyer, apibuyer
from AppStore.models import Class_Info


@buyer.route('/buyer/index/')
def index():
    return 'Hello World! This is buyer index.'


@buyer.route('/api/buyer/page/')
def page():
    return render_template('buyer/page.html')


@buyer.route('/buyer/data/')
def demo_data():
    return render_template('buyer/datapage.html')


@apibuyer.resource('/api/buyer/')
class BuyerApi(Resource):

    def __init__(self, *args, **kwargs):
        super(BuyerApi, self).__init__(*args, **kwargs)
        self.ret = {
            'code': 200,
            'version': 1.0,
            'frame': 'flask 1.1.1',
            'data': []
        }

    def get(self):
        class_all = Class_Info.query.all()
        
        print(type(class_all))  # <class 'list'>
        for obj in class_all:
            obj_data = {
                'class_num': obj.class_num,
                'class_name': obj.class_name,
                'entrance_time': obj.entrance_time.strftime('%Y-%m-%d'),
                'college': obj.college,
            }
            # print(type(obj.entrance_time))
            # new_date = obj.entrance_time.strftime('%Y-%m-%d')
            # print(new_date)
            # print(type(new_date))
            self.ret['data'].append(obj_data)
            # print(self.ret)
        return self.ret

    def post(self):
        data = request.form
        class_obj = Class_Info()

        class_obj.class_num = data.get('class_num')
        class_obj.class_name = data.get('class_name')
        class_obj.entrance_time = data.get('entrance_time')
        class_obj.college = data.get('college')
        class_obj.save()
        self.ret['data'] = '保存成功'
        return self.ret

    def put(self):
        return self.ret

    def delete(self):
        return self.ret
