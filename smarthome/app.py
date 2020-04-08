# coding:utf-8
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

import json

from config import Config

from huawei_sdk.client.concreteapi.PostCommandApi import postCommand
from huawei_sdk.client.concreteapi.SubscriptionApi import subscribe
from smarthome.PushMessageReceiver import receiver

# 创建flask的应用对象
app = Flask(__name__)

# 加载配置文件
app.config.from_object(Config)

# 获取数据库对象
db = SQLAlchemy(app)

# 注册SDK内部处理https请求的蓝图
app.register_blueprint(receiver)

from smarthome.models import HomeData

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/commands', methods=['GET', 'POST'])
def post_command():
    if request.method == 'GET':
        return jsonify(code=200, status=200, message="success", data={'name': '请求方式错误'})
    elif request.method == 'POST':
        data = request.json
        if not data:
            return jsonify(code=200, status=101, message="error:data empty", data={'name': '请求数据为空'})
        # print(data)
        method = data.get("method")
        paras = data.get("paras")
        if not method or not paras:
            return jsonify(code=200, status=102, message="error:paras empty", data={'name': '参数不全'})
        elif method == '' or paras == '':
            return jsonify(code=200, status=103, message="error:paras is empty str", data={'name': '参数为空字符串'})

        sp = postCommand(method, paras)

        result_commandId = json.loads(sp)['commandId']
        result_appId = json.loads(sp)['appId']
        result_deviceId = json.loads(sp)['deviceId']
        result_method = json.loads(sp)['command']['method']
        result_paras = json.loads(sp)['command']['paras']
        result_status = json.loads(sp)['status']
        result = {
            'commandId': result_commandId,
            'appId': result_appId,
            'deviceId': result_deviceId,
            'status': result_status,
            'method': result_method,
            'paras': result_paras
        }
        return jsonify(code=200, status=201, message="success", data=result)


@app.route('/subscription', methods=['GET'])
def subscription():
    notifyType = 'deviceDataChanged'
    callbackUrl = 'http://121.36.66.216:80/v1.0.0/messageReceiver'
    result = subscribe(notifyType, callbackUrl)
    return jsonify(code=200, message="subscribe success !", data=result)


@app.route('/db', methods=['POST'])
def save():
    data = request.json

    temperature = data['service']['data']['temperature_parlour_room']
    humidity = data['service']['data']['humidity_parlour_room']
    smoke = data['service']['data']['smoke_parlour_room']
    time = data['service']['eventTime']

    data_bean = HomeData()
    data_bean.temperature = temperature
    data_bean.humidity = humidity
    data_bean.smoke = smoke
    data_bean.time = time
    print(data_bean.temperature)

    db.session.add(data_bean)
    db.session.commit()

    return "ok"


if __name__ == '__main__':
    # 定时任务
    # scheduler = APScheduler()
    # # it is also possible to enable the API directly
    # scheduler.api_enabled = True
    # scheduler.init_app(app)
    # scheduler.start()

    # 数据库测试
    # from models import HomeData
    # temperature = db.Column(db.String(5), nullable=False)
    # humidity = db.Column(db.String(5), nullable=False)
    # smoke = db.Column(db.String(5), nullable=False)
    # time = db.Column(db.String(32), nullable=False)

    db.drop_all()
    db.create_all()
    app.run()
