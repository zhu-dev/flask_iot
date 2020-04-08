# -*- coding: utf-8 -*-
# @Author  : zhu

# base flask extend
from flask import Blueprint
from flask import render_template
from flask import request
from flask import json
from flask import jsonify

# import logging
from flask import current_app

# import db,models
from . import db, models

# import huawei libs
from huawei_sdk.client.concreteapi.PostCommandApi import postCommand
from huawei_sdk.client.concreteapi.SubscriptionApi import subscribe
from .models import HomeData, HomeData_Kitchen, HomeData_Bedroom
from .utils.TimeUtil import formatGMTime

app_main = Blueprint("main_app", __name__, static_folder='static', template_folder='templates')


@app_main.route('/')
@app_main.route('/index')
def index():
    return render_template('index.html')


@app_main.route('/commands', methods=['GET', 'POST'])
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
        print("method=%s,paras=%s", method, paras)
        if not method or not paras:
            return jsonify(code=200, status=102, message="error:paras empty", data={'name': '参数不全'})
        elif method == '' or paras == '':
            return jsonify(code=200, status=103, message="error:paras is empty str", data={'name': '参数为空字符串'})

        sp = postCommand(method, paras)
        print(sp)
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


@app_main.route('/subscription', methods=['GET'])
def subscribe():
    notifyType = 'deviceDataChanged'
    callbackUrl = 'http://121.36.66.216:80/v1.0.0/messageReceiver'
    result = subscribe(notifyType, callbackUrl)
    return jsonify(code=200, message="subscribe success !", data=result)


@app_main.route('/home_data', methods=['GET'])
def get_home_data():
    """
    1.android client 获取数据的接口
    2.以GET的参数区别要获取的数据
    3.参数 room: parlour|bedroom|kitchen->String
    """
    param = request.args.get("room")

    if param:

        if param == "parlour":
            # 获取客厅数据
            result = HomeData.query.filter().order_by(HomeData.id.desc()).first()
            if result:
                lcoal_time = formatGMTime(result.time)
                return jsonify(code=200,
                               message="query success ",
                               data={
                                   "temperature": result.temperature,
                                   "humidity": result.humidity,
                                   "smoke": result.smoke,
                                   "time": lcoal_time})
            else:
                return jsonify(code=201, message="result empty", data=None)

        elif param == "bedroom":
            # 获取卧室数据
            result = HomeData.query.filter().order_by(HomeData_Bedroom.id.desc()).first()
            if result:
                lcoal_time = formatGMTime(result.time)
                return jsonify(code=200,
                               message="query success ",
                               data={
                                   "temperature": result.temperature,
                                   "humidity": result.humidity,
                                   "smoke": result.smoke,
                                   "time": lcoal_time})
            else:
                return jsonify(code=201, message="result empty", data=None)

        elif param == "kitchen":
            # 获取厨房数据
            result = HomeData.query.filter().order_by(HomeData_Kitchen.id.desc()).first()
            if result:
                lcoal_time = formatGMTime(result.time)
                return jsonify(code=200,
                               message="query success ",
                               data={
                                   "temperature": result.temperature,
                                   "humidity": result.humidity,
                                   "smoke": result.smoke,
                                   "time": lcoal_time})
            else:
                return jsonify(code=201, message="result empty", data=None)

    return jsonify(code=202, message="get args empty", data=None)


@app_main.route('/home_datas', methods=['GET'])
def get_home_datas():
    """这是留给网页请求批量数据的接口"""
    param = request.args.get("room")
    # if param == "parlour":
    #     return jsonify(code=2, message="request success", data={"temperatrue": "26", "room": param})
    # return jsonify(code=1, message="request failed", data=None)
    if param:

        if param == "parlour":
            # 获取客厅数据
            results = HomeData.query.filter().order_by(HomeData.id.desc()).limit(10)
            count = HomeData.query.filter().order_by(HomeData.id.desc()).limit(10).count()
            if results:
                data_list = []

                if count == 10:
                    for result in results:
                        lcoal_time = formatGMTime(result.time)
                        data = {
                            "temperature": result.temperature,
                            "humidity": result.humidity,
                            "smoke": result.smoke,
                            "time": lcoal_time}
                        data_list.append(data)

                    return jsonify(code=2, message="request success", data=data_list)
                elif 0 < count < 10:
                    add = 10 - count

                    for result in results:
                        lcoal_time = formatGMTime(result.time)
                        data = {
                            "temperature": result.temperature,
                            "humidity": result.humidity,
                            "smoke": result.smoke,
                            "time": lcoal_time}
                        data_list.append(data)

                    for i in range(0, add):
                        data = {
                            "temperature": "0",
                            "humidity": "0",
                            "smoke": "0",
                            "time": "2020-01-01 00:00:00"
                        }
                        data_list.append(data)

                    return jsonify(code=2, message="request success", data=data_list)
            else:
                return jsonify(code=1, message="result empty", data=None)



        elif param == "bedroom":
            # 获取卧室数据
            results = HomeData_Bedroom.query.filter().order_by(HomeData_Bedroom.id.desc()).limit(10)
            count = HomeData_Bedroom.query.filter().order_by(HomeData_Bedroom.id.desc()).limit(10).count()
            if results:
                data_list = []

                if count == 10:
                    for result in results:
                        lcoal_time = formatGMTime(result.time)
                        data = {
                            "temperature": result.temperature,
                            "humidity": result.humidity,
                            "smoke": result.smoke,
                            "time": lcoal_time}
                        data_list.append(data)

                    return jsonify(code=2, message="request success", data=data_list)
                elif 0 < count < 10:
                    add = 10 - count

                    for result in results:
                        lcoal_time = formatGMTime(result.time)
                        data = {
                            "temperature": result.temperature,
                            "humidity": result.humidity,
                            "smoke": result.smoke,
                            "time": lcoal_time}
                        data_list.append(data)

                    for i in range(0, add):
                        data = {
                            "temperature": "0",
                            "humidity": "0",
                            "smoke": "0",
                            "time": "2020-01-01 00:00:00"
                        }
                        data_list.append(data)

                    return jsonify(code=2, message="request success", data=data_list)
            else:
                return jsonify(code=1, message="result empty", data=None)

        elif param == "kitchen":
            # 获取厨房数据
            results = HomeData_Kitchen.query.filter().order_by(HomeData_Kitchen.id.desc()).limit(10)
            count = HomeData_Kitchen.query.filter().order_by(HomeData_Kitchen.id.desc()).limit(10).count()
            if results:
                data_list = []

                if count == 10:
                    for result in results:
                        lcoal_time = formatGMTime(result.time)
                        data = {
                            "temperature": result.temperature,
                            "humidity": result.humidity,
                            "smoke": result.smoke,
                            "time": lcoal_time}
                        data_list.append(data)

                    return jsonify(code=2, message="request success", data=data_list)
                elif 0 < count < 10:
                    add = 10 - count

                    for result in results:
                        lcoal_time = formatGMTime(result.time)
                        data = {
                            "temperature": result.temperature,
                            "humidity": result.humidity,
                            "smoke": result.smoke,
                            "time": lcoal_time}
                        data_list.append(data)

                    for i in range(0, add):
                        data = {
                            "temperature": "0",
                            "humidity": "0",
                            "smoke": "0",
                            "time": "2020-01-01 00:00:00"
                        }
                        data_list.append(data)

                    return jsonify(code=2, message="request success", data=data_list)
            else:
                return jsonify(code=1, message="result empty", data=None)

    return jsonify(code=3, message="get args empty", data=None)
